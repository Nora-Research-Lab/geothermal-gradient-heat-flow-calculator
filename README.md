![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Geothermal Gradient & Heat Flow Calculator
 
*For geothermal geologists and engineers: enter surface and bottom temperatures, depth, and rock thermal conductivity to compute the geothermal gradient and heat flow, plus an automatic gradient classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geothermal Energy
 
This tool calculates the geothermal gradient and conductive heat flow from well temperature measurements and rock thermal conductivity. The user provides four numerical inputs: (1) Surface temperature (Ts, in °C, range -10 to 50), (2) Bottom temperature (Tb, in °C, range Ts to 500), (3) Depth (z, in meters, range 10 to 10000), and (4) Thermal conductivity (k, in W/m·K, range 0.1 to 5.0). Step-by-step logic: (a) Compute the geothermal gradient G = (Tb - Ts) / z, reported in °C/km by multiplying by 1000. (b) Compute conductive heat flow q = G * k (converted to consistent units: G in °C/m multiplied by k in W/m·K gives W/m²; also reported in mW/m² by multiplying by 1000). (c) Classify the gradient: <25 °C/km as 'Low', 25–35 °C/km as 'Normal', >35 °C/km as 'High' (favorable for geothermal). The Gradio UI shows four numeric inputs with labels and units, a 'Calculate' button, and three output areas: (i) a text display showing Geothermal Gradient (with classification), Heat Flow (in mW/m²), (ii) a simple matplotlib bar chart comparing the computed gradient to the normal-range band (25–35), and (iii) a downloadable CSV of inputs and outputs. Error handling: ensure Tb > Ts and z > 0, else show validation message. No AI/ML component.
 
## Run it
 
```bash
docker build -t geothermal-gradient-heat-flow-calculator .
docker run -p 7860:7860 geothermal-gradient-heat-flow-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-20.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
