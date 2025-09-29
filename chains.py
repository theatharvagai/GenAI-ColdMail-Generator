import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="deepseek-r1-distill-llama-70b")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Atharva, an M.Tech CSE student at VIT Vellore with a strong foundation in computer science, 
            AI, and software development. You are applying to the company for the role described above. 
            
            In your email:
            - Express enthusiasm for the role and appreciation for the company’s work.
            - Highlight your M.Tech studies, research paper ("Tourist Guide AI"), and relevant coding/AI projects.
            - Briefly mention that you are committed, disciplined, and eager to contribute.
            - Add the most relevant ones from the following links (treat them as your GitHub/portfolio links): {link_list}
            - Keep the tone professional, polite, and enthusiastic.
            
            Do not provide a preamble.
            
            ### EMAIL (NO PREAMBLE):
            
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        content = res.content
        if "<think>" in content:
            content = content.split("</think>")[-1].strip()

        return content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))