from flask import Flask, render_template, request
from AI import (
    idea_validator,
    problem_solver,
    marketing_asisstant,
    bussiness_plan_maker
)
from db import (
    save_idea,
    save_problem,
    save_marketing,
    save_business_plan,

    get_idea_history,
    get_problem_history,
    get_marketing_history,
    get_business_plan_history
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/idea-validator", methods=["GET", "POST"])
def idea():

    result = None

    if request.method == "POST":

        business_idea = request.form["business_idea"]
        business_type = request.form["business_type"]
        budget = request.form["budget"]
        extra_info = request.form["extra_info"]

        result = idea_validator(
            business_idea,
            business_type,
            budget,
            extra_info
        )
        save_idea(
        business_idea,
        business_type,
        budget,
        extra_info,
        result
            )

    return render_template(
        "idea_validator.html",
        result=result
    )

    


@app.route("/problem-solver", methods=["GET", "POST"])
def problem():
    result=None

    if request.method == "POST":

        problem = request.form["problem"]
        budget = request.form["budget"]
        business_type = request.form["business_type"]
        extra_info = request.form["extra_info"]

        result = problem_solver(
            problem,
            budget,
            business_type,
            extra_info
        )

        save_problem(
                problem,
                business_type,
                budget,
                extra_info,
                result
            )

    return render_template(
        "problem_solver.html",
        result=result
    )

    


@app.route("/marketing", methods=["GET", "POST"])
def marketing():
    result=None

    if request.method == "POST":

        result = marketing_asisstant(
            request.form["business_idea"],
            request.form["business_type"],
            request.form["marketing_budget"],
            request.form["target_audience"],
            request.form["business_goals"],
            request.form["extra_info"],
            request.form["marketing_idea"]
        )

        save_marketing(
                request.form["business_idea"],
                request.form["business_type"],
                request.form["marketing_budget"],
                request.form["target_audience"],
                request.form["business_goals"],
                request.form["extra_info"],
                request.form["marketing_idea"],
                result
            )
        


    return render_template(
        "marketing.html",
        result=result
    )

    
@app.route("/business-plan", methods=["GET", "POST"])
def business_plan():
    result=None

    if request.method == "POST":

        info = request.form["additional_information"]

        result = bussiness_plan_maker(info)

        save_business_plan(
                info,
                result
                )
        
        
        

    return render_template(
        "business_plan.html",
        result=result
    )



@app.route("/history")
def history():

    ideas = get_idea_history()

    problems = get_problem_history()

    marketing = get_marketing_history()

    plans = get_business_plan_history()

    return render_template(
        "history.html",

        ideas=ideas,

        problems=problems,

        marketing=marketing,

        plans=plans
    )






if __name__ == "__main__":
    app.run(debug=True)


