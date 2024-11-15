from Models.school_model import School, db

class SchoolRepository:
    @staticmethod
    def add_school(name, description):
        new_school = School(name=name, description=description)
        db.session.add(new_school)
        db.session.commit()
        return new_school
    
    @staticmethod
    def get_all_schools():
        return School.query.all()
    
    @staticmethod
    def get_school_by_id(school_id):
        return School.query.get(school_id)
    
    @staticmethod
    def delete_school(school_id):
        school = School.query.get(school_id)
        if school:
            db.session.delete(school)
            db.session.commit()
            return True
        return False