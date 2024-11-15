from Repositories.school_repository import SchoolRepository

class SchoolService:
    @staticmethod
    def add_school(data):
        name = data.get('name')
        description = data.get('description')
        return SchoolRepository.add_school(name, description)
    
    @staticmethod
    def get_all_schools():
        return SchoolRepository.get_all_schools()

    @staticmethod
    def get_school_by_id(school_id):
        return SchoolRepository.get_school_by_id(school_id)
    
    @staticmethod
    def delete_school(school_id):
        return SchoolRepository.delete_school(school_id)
