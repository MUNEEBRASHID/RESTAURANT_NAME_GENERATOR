from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")


llm=OpenAI(temperature=0.8)

def restaurant_name_and_items_generator(Cuisine):
    #Chain 1: Restaurant Name
    prompt_template=PromptTemplate(
    input_variable=['Cuisine'],
    template="I want to open a restaorant {Cuisine} food. Suggest me a name for the restaurant. Only one name please."
    )

    name_chain=LLMChain(llm=llm,prompt=prompt_template,output_key='restaurant_name')

    #Chain 2:Menu Items
    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name', 'Cuisine'],
        template="""For the {Cuisine} restaurant named "{restaurant_name}", create a menu with 10 items.
        
        For each item, list its name followed by its main ingredients.
        Format each item as follows:
        Item Name: [item name]
        Ingredients: [ingredient 1], [ingredient 2], [ingredient 3]

        Provide all 10 items in this format and with only 3 main ingredients."""
    )

    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key='menu_items')

    

    chain=SequentialChain(chains=[name_chain,food_items_chain],
                input_variables=['Cuisine'],
                output_variables=['restaurant_name','menu_items'])
    response=chain.invoke({'Cuisine':Cuisine})

    return response

if __name__=="__main__":
    print(restaurant_name_and_items_generator("Italian"))




