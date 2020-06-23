/* Javascript for GradeXBlock. */
function GradeXBlock(runtime, element) {

    function updateGrade(result) {
        $('#pre_grade', element).text(result.grade);
    }

    var handlerUrl = runtime.handlerUrl(element, 'save_grades');

    $('#submit', element).click(function(eventObject) {

        let student = document.getElementById("student").value;
        let grade = document.getElementById("grade").value;

        $.ajax({
            type: "POST",
            url: handlerUrl,
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            data: JSON.stringify({"student": student, "grade": grade}),
            success: updateGrade
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
