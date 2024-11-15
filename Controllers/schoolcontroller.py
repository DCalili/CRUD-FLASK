from flask import jsonify, request, make_response
from Services.schoolservices import SchoolService

class SchoolController:
    @staticmethod
    def get_schools():
        schools = SchoolService.get_all_schools()
        return jsonify([{"id": school.id, "name": school.name, "description": school.description} for school in schools])
    
    @staticmethod
    def add_school():
        data = request.get_json()
        new_school = SchoolService.add_school(data)
        return make_response(jsonify({"id": new_school.id, "name": new_school.name, "description": new_school.description}))
    
    @staticmethod
    def get_school(school_id):
        school = SchoolService.get_school_by_id(school_id)
        if school:
            return jsonify({"id": school.id, "name": school.name, "description": school.description})
        return jsonify({"message": "School not found"}), 404
    
    @staticmethod
    def delete_school(school_id):
        if SchoolService.delete_school(school_id):
            return jsonify({"message": "School deleted successfully"}), 200
        return jsonify({"message": "School not found"}), 404