import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the Model (using gpt-4o for multimodality)
model = ChatOpenAI(model="gpt-4o")

# 2. Create the Output Parser
output_parser = StrOutputParser()

# 3. Handle Multimodal Input
def chat_response(message, history):
    text = message["text"]
    # Image handling logic can be added here
    response = model.invoke(text)
    return output_parser.invoke(response)

# 4. Themes and Colors (Blue Background and Cream Text)
custom_theme = gr.themes.Soft(
    primary_hue="blue", 
    secondary_hue="sky",
).set(
    body_background_fill="*neutral_950", # Very dark, appears blackish-blue
    body_text_color="*primary_900",    # Creamy/light blue text
    button_primary_background_fill="*primary_500",
)

# 5. Multimodal ChatInterface with Description and Theme
demo = gr.ChatInterface(
    fn=chat_response,
    title="AI Assistant",
    description="Created by Rajan", # Adds your name!
    theme=custom_theme,
    multimodal=True 
)

demo.launch()
app = demo.app
