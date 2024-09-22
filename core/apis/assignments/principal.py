from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.apis.teachers import TeacherSchema
from core.models.assignments import Assignment
from core.models.teachers import Teacher
from .schema import AssignmentSchema, AssignmentGradeSchema

# Define a new blueprint for principal-related assignment resources
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of all submitted and graded assignments for the principal."""
    # Retrieve assignments that are either submitted or graded
    principal_assignments = Assignment.get_all_submitted_and_graded()
    
    # Serialize the assignments data
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    
    # Return the serialized data as a response
    return APIResponse.respond(data=principal_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_or_regrade_assignment(p, incoming_payload):
    """Grade or re-grade an assignment"""
    # Validate and load the incoming payload using AssignmentGradeSchema
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    
    # Mark or re-grade the assignment with the specified grade
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        teacher_id = None,
        auth_principal=p  # Ensure the action is authorized by the principal
    )
    
    # Commit the transaction to save changes to the database
    db.session.commit()
    
    # Serialize the updated assignment data
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    
    # Return the serialized data as a response
    return APIResponse.respond(data=graded_assignment_dump)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns a list of all teachers"""
    # Retrieve all teacher records from the database
    all_teachers = Teacher.get_all_teachers()
    
    # Serialize the teacher data using TeacherSchema
    all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
    
    # Return the serialized data as a response
    return APIResponse.respond(data=all_teachers_dump)
