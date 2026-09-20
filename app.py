import gradio as gr
import pandas as pd
from geothermal_gradient_heat_flow_calculator import calculate_geothermal_properties, validate_inputs

def process_calculation(surface_temp, bottom_temp, depth, thermal_conductivity):
    # Validate inputs
    is_valid, error_msg = validate_inputs(surface_temp, bottom_temp, depth, thermal_conductivity)
    if not is_valid:
        return error_msg, None, None
    
    # Perform calculations
    gradient, heat_flow_mw_per_m2, classification = calculate_geothermal_properties(
        surface_temp, bottom_temp, depth, thermal_conductivity
    )
    
    # Prepare results text
    results_text = f"""
Geothermal Gradient: {gradient:.2f} °C/km ({classification})
Conductive Heat Flow: {heat_flow_mw_per_m2:.2f} mW/m²
"""
    
    # Create visualization
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Plot the calculated gradient
    ax.bar(['Calculated Gradient'], [gradient], color='blue', alpha=0.7, label='Calculated Gradient')
    
    # Add normal range band (25-35 °C/km)
    ax.axhspan(25, 35, color='green', alpha=0.3, label='Normal Range (25-35 °C/km)')
    
    ax.set_ylabel('Gradient (°C/km)')
    ax.set_title('Geothermal Gradient vs Normal Range')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Create CSV data
    csv_data = {
        'Parameter': ['Surface Temperature (°C)', 'Bottom Temperature (°C)', 'Depth (m)', 'Thermal Conductivity (W/m·K)', 
                      'Geothermal Gradient (°C/km)', 'Heat Flow (mW/m²)', 'Classification'],
        'Value': [surface_temp, bottom_temp, depth, thermal_conductivity, gradient, heat_flow_mw_per_m2, classification]
    }
    df = pd.DataFrame(csv_data)
    
    return results_text, fig, df

with gr.Blocks() as demo:
    gr.Markdown("## Geothermal Gradient & Heat Flow Calculator")
    gr.Markdown("Calculate geothermal gradient and conductive heat flow from temperature and depth measurements.")
    
    with gr.Row():
        surface_temp = gr.Number(label="Surface Temperature (°C)", value=20, minimum=-10, maximum=50)
        bottom_temp = gr.Number(label="Bottom Temperature (°C)", value=100, minimum=-9, maximum=500)
    
    with gr.Row():
        depth = gr.Number(label="Depth (m)", value=1000, minimum=10, maximum=10000)
        thermal_conductivity = gr.Number(label="Thermal Conductivity (W/m·K)", value=2.5, minimum=0.1, maximum=5.0)
    
    calculate_btn = gr.Button("Calculate")
    
    with gr.Column():
        results_output = gr.Textbox(label="Results", interactive=False)
        plot_output = gr.Plot(label="Gradient Visualization")
        csv_output = gr.Dataframe(label="Download Results as CSV")
    
    calculate_btn.click(
        fn=process_calculation,
        inputs=[surface_temp, bottom_temp, depth, thermal_conductivity],
        outputs=[results_output, plot_output, csv_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
