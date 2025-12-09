from .. import db
from datetime import datetime

class VMRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vm_type = db.Column(db.String(50))  # bronze, silver, gold
    status = db.Column(db.String(20), default='pending')  # pending/approved/denied
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50))  
    hostname = db.Column(db.String(50))  
    ssh_key = db.Column(db.Text) 
