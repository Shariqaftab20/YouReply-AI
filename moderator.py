from openai import OpenAI
from fastapi import FastAPI, Request
import json
import os


# # to start the server type this in command line 

# uvicorn <moderator>:app --reload  

app = FastAPI()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)


@app.get("/health-check")
def sayHello():
    return { "message": "api working" }

@app.post("/comment")
async def moderator(request: Request):
    requestBody = await request.json()
    comment = requestBody["comment"]

    moderation = client.moderations.create(input=comment)
    response = moderation.results[0]
    entry = {
            "input": comment,
            "Result": {
                    "flagged": response.flagged,
                    "categories": {
                        "sexual": response.categories.sexual,
                        "hate": response.categories.hate,
                        "harassment": response.categories.harassment,
                        "self-harm": response.categories.self_harm,
                        "sexual/minors": response.categories.sexual_minors,
                        "hate/threatening": response.categories.hate_threatening,
                        "violence/graphic": response.categories.violence_graphic,
                        "self-harm/intent": response.categories.self_harm_intent,
                        "self-harm/instructions": response.categories.self_harm_instructions,
                        "harassment/threatening": response.categories.harassment_threatening,
                        "violence": response.categories.violence,
                    },
                    "category_scores": {
                        "sexual": response.category_scores.sexual,
                        "hate": response.category_scores.hate,
                        "harassment": response.category_scores.harassment,
                        "self-harm": response.category_scores.self_harm,
                        "sexual/minors": response.category_scores.sexual_minors,
                        "hate/threatening": response.category_scores.hate_threatening,
                        "violence/graphic": response.category_scores.violence_graphic,
                        "self-harm/intent": response.category_scores.self_harm_intent,
                        "self-harm/instructions": response.category_scores.self_harm_instructions,
                        "harassment/threatening": response.category_scores.harassment_threatening,
                        "violence": response.category_scores.violence,
                    }
                    
            }
    }

    return entry 

def moderator(comment):
    moderation = client.moderations.create(input=comment)
    response = moderation.results[0]
    entry = {
            "input": comment,
            "Result": {
                    "flagged": response.flagged,
                    "categories": {
                        "sexual": response.categories.sexual,
                        "hate": response.categories.hate,
                        "harassment": response.categories.harassment,
                        "self-harm": response.categories.self_harm,
                        "sexual/minors": response.categories.sexual_minors,
                        "hate/threatening": response.categories.hate_threatening,
                        "violence/graphic": response.categories.violence_graphic,
                        "self-harm/intent": response.categories.self_harm_intent,
                        "self-harm/instructions": response.categories.self_harm_instructions,
                        "harassment/threatening": response.categories.harassment_threatening,
                        "violence": response.categories.violence,
                    },
                    "category_scores": {
                        "sexual": response.category_scores.sexual,
                        "hate": response.category_scores.hate,
                        "harassment": response.category_scores.harassment,
                        "self-harm": response.category_scores.self_harm,
                        "sexual/minors": response.category_scores.sexual_minors,
                        "hate/threatening": response.category_scores.hate_threatening,
                        "violence/graphic": response.category_scores.violence_graphic,
                        "self-harm/intent": response.category_scores.self_harm_intent,
                        "self-harm/instructions": response.category_scores.self_harm_instructions,
                        "harassment/threatening": response.category_scores.harassment_threatening,
                        "violence": response.category_scores.violence,
                    }
                    
            }
    }
    return entry 


@app.post("/process-comments")
async def processAllComments(request: Request):
    requestBody = await request.json()
    comments = requestBody["comments"]

    print(comments)

    return { "msg": "ok" }
