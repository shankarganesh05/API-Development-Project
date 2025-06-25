from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from typing import List
from ..database import get_session
from .. import model,schemas,utils,outh2
from sqlmodel import select,Session

router = APIRouter(prefix="/vote",tags=["vote"])

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_vote(vote:schemas.Vote,db:Session = Depends(get_session),current_user:int = Depends(outh2.get_current_user)):
    vote_query = db.exec(select(model.Vote).filter(model.Vote.post_id==vote.post_id,model.Vote.user_id==current_user.id))
    found_vote = vote_query.first()
    if vote.dir == True:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,details=f"Vote for post {vote.post_id} already exist")
        new_vote = model.Vote(post_id = vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Successfully added your vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Vote doesn't exist")
        db.delete(found_vote)
        db.commit()
        return {"message": "Successfully deleted your vote"}
    
        
        
