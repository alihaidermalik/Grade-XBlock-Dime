"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblockutils.resources import ResourceLoader
from xblock.fields import Integer, Scope, String

loader = ResourceLoader(__name__)

class GradeXBlock(XBlock):
    """
    GradeXBlock: say Hi! to the logged in student and save the student desire grade.
    """

    student = String(
        scope=Scope.user_state,
        help="user name of the student",
    )

    grade = Integer(
        default=0, scope=Scope.user_state,
        help="Store the desire grade of a student",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the GradeXBlock, shown to students
        when viewing courses.
        """
        user_service = self.runtime.service(self, 'user')
        xb_user = user_service.get_current_user()

        context.update({
            "self": self,
            "username": xb_user.full_name
        })

        fragment = Fragment()
        fragment.add_content(loader.render_template("static/html/gradexblock.html",context))
        fragment.add_javascript(self.resource_string("static/js/src/gradexblock.js"))
        fragment.initialize_js('GradeXBlock')
        return fragment

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_grades(self, data, suffix=''):
        """
        Save the data of grades from student and student username as well.
        """
        self.student = data['student']
        self.grade = data['grade']

        return {"grade": self.grade}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GradeXBlock",
             """<gradexblock/>
             """),
            ("Multiple GradeXBlock",
             """<vertical_demo>
                <gradexblock/>
                <gradexblock/>
                <gradexblock/>
                </vertical_demo>
             """),
        ]
