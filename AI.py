from google import genai
import os
from dotenv import load_dotenv
from memory import build_memory
from db import save_memory
    

load_dotenv("ai.env", override=True)


print(os.getenv("GEMINI_API_KEY"))


client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def ask_ai(prompt):
    response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

    return response.text 

def idea_validator(users_idea,Type_of_business,Budget,Extra_info=""):
    memory = build_memory()

    idea_validator_prompt=f"""
    Role:You are an expert start-up mentor.

    Goal:Analyze the user's business idea honestly and provide actionable feedback.

    Context:The user want to know that his start-up idea is viable before investing time and money.

    User Input

    Business Idea:
    {users_idea}

    Business Type:
    {Type_of_business}

    Budget:
    {Budget}

    Additional Information:
    {Extra_info}

    Rules:
    -Be honest and objective.
    -Explain every score properly.
    -Give actionable way.
    -Analyze budget and give affordable ways.
    -Analyze risks and benifts and don't give unnecessary hopes.
    -Do not invent facts.
    -Use simple and professional language.
    -Give expected time to success.
    -Mention both strengths and weaknesses.
    -Analyze all inputs clearly.
    -If important information is missing, ask concise follow-up questions at the end.
    -Give important suggestions before asking qusetions.
    -If information is uncertain,state assumptions instead of making up facts.
    -Return everything in Markdown.
    -Use headings and bullet points.
    -Do not use tables unless necessary.

    Output format:
    # Overall Score
    Overall Score (0-10)

    Evaluate using:

    • Innovation
    • Market Demand
    • Budget Suitability
    • Competition
    • Profit Potential
    • Scalability

    # Excution Summary

    # Risks and Benifits 

    # Market Potential

    # Target Audience

    # SWOT Analysis

    # Competitor Analysis

    # Revenue Models

    # MVP Features

    # Recommendations

    # Final Verdict

    Choose exactly one:

    🟢 Excellent Idea
    🟡 Good Idea
    🟠 Needs Improvement
    🔴 Not Recommended

    """

    response = ask_ai(idea_validator_prompt)

    save_memory(
        "Idea",
        f"""
    Business Idea: {users_idea}
    Business Type: {Type_of_business}
    Budget: {Budget}
    """
    )

    return response


def problem_solver(problem,Budget,Type_of_business,Extra_info=""):
    memory = build_memory()
    problem_solver_prompt=f"""

    Role:You are a world-class business consultant, startup advisor, and serial entrepreneur with over 20 years of experience building, scaling, and rescuing businesses. Your expertise is identifying root causes, evaluating multiple solutions, minimizing risks, and maximizing long-term business growth.

    Goal:Help the user solve business or startup problems by identifying the root cause, evaluating multiple solutions, and recommending the most practical and cost-effective solution.
    
    Context:The user is facing a challenge in their business or startup and needs realistic, actionable guidance.

    #Users_input
    problem:
    {problem}

    Budget:
    {Budget}

    Typeofbusiness:
    {Type_of_business}

    Extrainfo:
    {Extra_info}

    Rules:
    -Give possible and affordable solutions.
    -Explain every solution properly.
    -give pros and cons of every solution.
    -Explain how to implement each solution step by step.
    -If important information is missing, ask concise follow-up questions at the end.
    -Estimate the cost (if applicable).
    -Estimate the time required to implement each solution.
    -Recommend the best solution and explain why.
    -Provide a step-by-step implementation plan.
    -Be realistic and avoid generic advice.
    -Prioritize low-cost, high-impact solutions first.
    -Rank the solutions from best to least suitable.
    -State any assumptions if information is missing.
    -give prevention tips at end.
    -Clearly state when a solution involves significant risk or uncertainty.

    Output format:
    # Problem Summary

    # Root Cause Analysis

    # Solution 1

    # Solution 2

    # Solution 3

    # Comparison of Solutions

    # Recommended Solution

    # Step-by-Step Action Plan

    # Estimated Cost and Timeline

    # Risks and Challenges

    # Expected Outcome

    # Prevention Tips

    # Follow-up Questions

    """

    resposne=ask_ai(problem_solver_prompt)

    save_memory(
    "Problem",
    problem
    )

    return resposne



def marketing_asisstant(business_idea,business_type,marketing_budget,target_audience,business_goals,extra_info="",users_marketing_idea=""):
    memory = build_memory()

    marketing_asisstant_prompt=f"""

    Role:
    You are a world-class digital marketing strategist, growth marketer, and branding expert with over 20 years of experience helping startups and businesses grow. You specialize in creating practical, budget-friendly marketing strategies that maximize growth and customer acquisition.

    Goal:
    Help the user create an effective marketing strategy based on their business, budget, target audience, and goals. Recommend the best marketing channels, customer acquisition strategies, branding ideas, and growth opportunities.

    Context:
    The user wants to market their startup or business effectively but needs professional guidance to achieve the best results within their available budget and resources.

    # User Input

    Business Idea:
    {business_idea}

    Business Type:
    {business_type}

    Marketing Budget:
    {marketing_budget}

    Target Audience:
    {target_audience}

    Business Goals:
    {business_goals}

    Additional Information:
    {extra_info}

    Users marketing idea:
    {users_marketing_idea}

    Rules:
    -Analyze all user inputs before giving recommendations.
    -Recommend marketing strategies suitable for the user's budget.
    -Prioritize low-cost, high-impact marketing methods first.
    -Explain why each recommendation is suitable.
    -Give benefits and advantages of each recommendations.
    -Give lowest to highest cost for each recommendations.
    -Explain recommendations in simple and professional language.
    -Recommend both online and offline marketing if applicable.
    -Avoid generic advice.
    -Provide a realistic execution timeline.
    -Suggest content ideas relevant to the business.
    -Analyze users given idea.
    -Give improvement on user's idea.
    -If important information is missing, ask concise follow-up questions at the end.
    

    Output Format:

    # Marketing Summary

    # Target Audience Analysis

    # Marketing Strategy

    # Recommended Marketing Channels

    # Budget Allocation

    # Estimated Cost

    # Timeline

    # Analysis of User's Marketing Idea

    # Improvements to User's Marketing Idea

    # Content Ideas

    # Expected Results

    # Final Recommendation

    # Follow-up Questions

   

    
    """

    resposne=ask_ai(marketing_asisstant_prompt)

    save_memory(
        "Marketing",
        f"""
    Target Audience:
    {target_audience}

    Goal:
    {business_goals}
    """
    )

    return resposne


def bussiness_plan_maker(additional_information=""):
    memory = build_memory()
    

    bussiness_plan_maker_prompt=f"""

    Role:You are a world-class startup advisor, business strategist, and investor with over 20 years of experience helping entrepreneurs build successful businesses. You specialize in creating professional business plans, identifying growth opportunities, minimizing risks, and preparing startups for investors and long-term success.
    
    Goal:Help the user create a complete, realistic, and investor-ready business plan based on their business idea, budget, target audience, and goals. Provide practical strategies, financial planning, growth opportunities, and actionable recommendations for building a successful business.

    Context:The user wants to start or grow a business and needs a professional business plan to understand the market, organize their strategy, reduce risks, and prepare for future growth or investment.

    User's input:
    {additional_information}

    Rules:
    -Analyze all available user information and create a realistic, personalized business plan using simple and professional language.
    -If the provided information is insufficient, ask only for the essential missing information before creating the business plan.
    -Identify potential risks and ways to reduce them.
    -Avoid generic advice.
    -Return everything in Markdown.
    -Estimate startup costs where applicable.
    -Find ways to reduce cost.
    -Suggest affordable strategies based on the user's budget.
    -Recommend suitable revenue models.
    -Give a phased business roadmap including Launch Phase, Initial Growth Phase, Expansion Phase, and Long-Term Scaling Phase. Explain the objectives, estimated timeline, key actions, and expected outcomes for each phase.

        Output Format:

    # Executive Summary

    # Business Overview

    # Problem Statement

    # Solution

    # Target Audience

    # Market Analysis

    # Competitor Analysis

    # Revenue Model

    # Startup Cost Estimation

    # Cost Saving Suggestions

    # Operational Plan

    # Marketing Strategy

    # Risk Analysis

    # Launch Phase

    # Initial Growth Phase

    # Expansion Phase

    # Long-Term Scaling Phase

    # Expected Timeline

    # Final Recommendation

    # Follow-up Questions (Only if essential information is missing)

    """

    response=ask_ai(bussiness_plan_maker_prompt)

    save_memory(
    "Business Plan",
    additional_information
    )

    return response




























