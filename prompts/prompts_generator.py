from langchain_core.prompts import PromptTemplate

template = PromptTemplate(template='Greet this person in {languages} languages. The name of the person is {name}',
                          input_variables=['name','languages'],
                          validate_template=True)

template.save('template.json')