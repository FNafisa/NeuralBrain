# for hosting on huggingface spaces : https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces

# pip install -r requirements.txt
import numpy as np
import gradio as gr
import os


def seperate_voices(the_input):
    return the_input # this function should call the model and do the magic
            
            
def exampels(inputs, outputs):

    gr.HTML("<h2>Try some examples</h2>")
    gr.HTML("<h2>Click on Recording.wav then run</h2>")

    path = os.path.join(os.getcwd(), "Recording.wav") # to get the example file path
    return gr.Examples(
            examples=[path],
            inputs= inputs,
            outputs=outputs,
            fn=seperate_voices(gr.Audio(path)),
        )


def generate_block():

    with gr.Blocks() as block:
      
        gr.HTML('<h1>NeuralBrain</h1>')
        gr.HTML("<h3>Seperate each voice from a group of voices</h3>")

        with gr.Tab("Uploding a file"):
            
            # See the behavior of the Audio object : https://www.gradio.app/docs/audio
            audio_input = gr.Audio() 
            audio_output = gr.Audio()
            file_button = gr.Button(text="Flip")
            exampels(audio_input, audio_output)

        with gr.Tab("Recording an audio"):
            
            with gr.Row():
                record_input = gr.Microphone()
                record_output = gr.Audio()
            record_button = gr.Button(text="Flip") 
            exampels(record_input, record_output)

        with gr.Accordion("The team"): # We should write everything here about our story
            gr.HTML("""
                    <h2>All credits reserved for the NeuralBrain team</h2>
                    <h3>Mamdouh Aldhafeeri - Fahad Alnafisa - Ahmed Alghouth - Ahmed Almohammed - Ghalia Alnanaih - Danah Almuhaysin </h3>
                    """)
      

        file_button.click(seperate_voices, inputs = audio_input, outputs=audio_output)
        record_button.click(seperate_voices, inputs=record_input, outputs=record_output)

    block.queue()
    block.launch()


def main():
    generate_block()

if __name__ == "__main__":
    main()

