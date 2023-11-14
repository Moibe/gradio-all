import gradio as gr

def speech_to_text(name):
    # speech to text here...
    return "This is the text"

demo = gr.Interface(fn=speech_to_text,
                    inputs=gr.Audio(label="Audio file"),
                    outputs=gr.Text())

demo.launch(debug=True)
    
# if __name__ == "__main__":
#     demo.launch(show_api=False)   