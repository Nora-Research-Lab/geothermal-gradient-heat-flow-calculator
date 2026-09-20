def calculate_geothermal_properties(surface_temp, bottom_temp, depth, thermal_conductivity):
    """
    Calculate geothermal gradient and conductive heat flow.
    
    Args:
        surface_temp (float): Surface temperature in °C
        bottom_temp (float): Bottom temperature in °C
        depth (float): Depth in meters
        thermal_conductivity (float): Thermal conductivity in W/m·K
    
    Returns:
        tuple: (gradient in °C/km, heat_flow in mW/m², classification string)
    """
    # Calculate geothermal gradient in °C/km
    gradient_c_per_km = (bottom_temp - surface_temp) / depth * 1000
    
    # Calculate conductive heat flow in W/m² then convert to mW/m²
    gradient_c_per_m = (bottom_temp - surface_temp) / depth
    heat_flow_w_per_m2 = gradient_c_per_m * thermal_conductivity
    heat_flow_mw_per_m2 = heat_flow_w_per_m2 * 1000
    
    # Classify the gradient
    if gradient_c_per_km < 25:
        classification = "Low"
    elif 25 <= gradient_c_per_km <= 35:
        classification = "Normal"
    else:
        classification = "High"
    
    return gradient_c_per_km, heat_flow_mw_per_m2, classification


def validate_inputs(surface_temp, bottom_temp, depth, thermal_conductivity):
    """
    Validate the input parameters.
    
    Args:
        surface_temp (float): Surface temperature in °C
        bottom_temp (float): Bottom temperature in °C
        depth (float): Depth in meters
        thermal_conductivity (float): Thermal conductivity in W/m·K
    
    Returns:
        tuple: (is_valid boolean, error_message string)
    """
    if depth <= 0:
        return False, "Depth must be greater than 0 meters."
    
    if bottom_temp <= surface_temp:
        return False, "Bottom temperature must be greater than surface temperature."
    
    if not (-10 <= surface_temp <= 50):
        return False, "Surface temperature must be between -10°C and 50°C."
    
    if not (surface_temp < bottom_temp <= 500):
        return False, f"Bottom temperature must be greater than surface temperature ({surface_temp}°C) and less than or equal to 500°C."
    
    if not (10 <= depth <= 10000):
        return False, "Depth must be between 10 and 10000 meters."
    
    if not (0.1 <= thermal_conductivity <= 5.0):
        return False, "Thermal conductivity must be between 0.1 and 5.0 W/m·K."
    
    return True, ""
