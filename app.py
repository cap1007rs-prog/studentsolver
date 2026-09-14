from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Create the Prompt Template
prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant that provides step-by-step solutions to math and science problems."),
      ("user", "{problem}")
])

# 2. Initialize the Model
model = ChatOpenAI(model="gpt-4o-mini")

# 3. Create the Output Parser
output_parser = StrOutputParser()

# 4. Combine into a Chain
chain = prompt | model | output_parser

# 5. Run the chain with your problem
problem_input = "solve 2x + 5 = 15"
response = chain.invoke({"problem": problem_input})

# 6. Print the result
print(response)
import gradio as gr

demo = gr.Interface(
    fn=lambda problem: chain.invoke({"problem": problem}),
    inputs=[gr.Textbox(label="Enter a problem", lines=1)],
    outputs=[gr.Textbox(label="Step-by-Step Solution", lines=10)],
    flagging_mode="never",
    title="Step-by-Step Problem Solver",
    description="Enter any math or science problem and get a clear solution",article='Created by Rajan',theme='glass'
)
demo.launch()

