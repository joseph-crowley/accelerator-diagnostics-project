
#########################################################################################
############## For use in the plot.py model - variable choices for the runs #############
#########################################################################################

RUN_VAR_CHOICES = [ # TODO: Update variable choices - standardize the naming and fix the units, remove duplicates
    ('none', 'None'),
    ('Area_CH1', 'Area of CH1 Pulse (nVs)'),
    ('Area_CH1_FullWaveform', 'Area of Full Waveform for CH1 (nVs)'),
    ('Area_CH2', 'Area of CH2 Pulse (nVs)'),
    ('Area_CH2_FullWaveform', 'Area of Full Waveform for CH2 (nVs)'),
    ('Area_CH3', 'Area of CH3 Pulse (nVs)'),
    ('Area_CH3_FullWaveform', 'Area of Full Waveform for CH3 (nVs)'),
    ('Area_CH4', 'Area of CH4 Pulse (nVs)'),
    ('Area_CH4_FullWaveform', 'Area of Full Waveform for CH4 (nVs)'),
    ('Area_General', 'Area of Pulse (nVs)'),
    ('CalibratedArea_CH1', 'Area of CH1 Pulse Calibrated into keV'),
    ('CalibratedArea_CH2', 'Area of CH2 Pulse Calibrated into keV'),
    ('CalibratedArea_CH3', 'Area of CH3 Pulse Calibrated into keV'),
    ('CalibratedArea_CH4', 'Area of CH4 Pulse Calibrated into keV'),
    ('CalibratedArea_General', 'Area of Pulse Calibrated into keV (if Calibration Available)'),
    ('ChannelNumber', 'Channel Number for Pulse'),
    ('EventNumber', 'Event Number'),
    ('EventTypeCode', 'Event Type Code (Run Dependent)'),
    ('HalfMaxHeightTime_CH1', 'Time When CH1 Pulse Crosses Half its Max Height'),
    ('HalfMaxHeightTime_CH2', 'Time When CH2 Pulse Crosses Half its Max Height'),
    ('HalfMaxHeightTime_CH3', 'Time When CH3 Pulse Crosses Half its Max Height'),
    ('HalfMaxHeightTime_CH4', 'Time When CH4 Pulse Crosses Half its Max Height'),
    ('LeadingEdgeSlope_CH1', 'Fitted Leading Slope for CH1 (mV/ns)'),
    ('LeadingEdgeSlope_CH2', 'Fitted Leading Slope for CH2 (mV/ns)'),
    ('LeadingEdgeSlope_CH3', 'Fitted Leading Slope for CH3 (mV/ns)'),
    ('LeadingEdgeSlope_CH4', 'Fitted Leading Slope for CH4 (mV/ns)'),
    ('LeadingEdgeStartTime_CH1', 'Fitted Start Time of Leading Edge for CH1 Pulse'),
    ('LeadingEdgeStartTime_CH2', 'Fitted Start Time of Leading Edge for CH2 Pulse'),
    ('LeadingEdgeStartTime_CH3', 'Fitted Start Time of Leading Edge for CH3 Pulse'),
    ('LeadingEdgeStartTime_CH4', 'Fitted Start Time of Leading Edge for CH4 Pulse'),
    ('NPECalibratedArea', 'Area of Pulse Calibrated into NPE (if Calibration Available)'),
    ('PulseCount_CH1', 'Number of Pulses in Channel 1 for Event'),
    ('PulseCount_CH2', 'Number of Pulses in Channel 2 for Event'),
    ('PulseCount_CH3', 'Number of Pulses in Channel 3 for Event'),
    ('PulseCount_CH4', 'Number of Pulses in Channel 4 for Event'),
    ('PulseNumberInEvent', 'Pulse Number Within the Event for Channel (0 is First Pulse)'),
    ('PulseTime_CH1', 'Approximate Time of CH1 Pulse'),
    ('PulseTime_CH2', 'Approximate Time of CH2 Pulse'),
    ('PulseTime_CH3', 'Approximate Time of CH3 Pulse'),
    ('PulseTime_CH4', 'Approximate Time of CH4 Pulse'),
    ('PulseTime_General', 'Time of Pulse Within Waveform (ns)'),
    ('PulseWidth', 'Width (Duration) of Pulse (ns)'),
    ('RMSNoise_CH1', 'RMS Noise Measured in Channel1'),
    ('RMSNoise_CH1_mV', 'RMS Noise Measured for CH1 (mV)'),
    ('RMSNoise_CH2', 'RMS Noise Measured in Channel2'),
    ('RMSNoise_CH2_mV', 'RMS Noise Measured for CH2 (mV)'),
    ('RMSNoise_CH3', 'RMS Noise Measured in Channel3'),
    ('RMSNoise_CH3_mV', 'RMS Noise Measured for CH3 (mV)'),
    ('RMSNoise_CH4', 'RMS Noise Measured in Channel4'),
    ('RMSNoise_CH4_mV', 'RMS Noise Measured for CH4 (mV)'),
    ('RMSNoise_General', 'RMS Noise Measured in the Channel Containing Pulse'),
    ('RunNumber', 'Run Number'),
    ('TimeBetweenEvents', 'Time Between Current and Previous Event (seconds)'),
    ('TimeInRun', 'Time Since Start of the Run (seconds)'),
    ('TotalPulseCount', 'Number of Pulses in Event Across All Channels'),
    ('Voltage_CH1', 'Height of CH1 Pulse (mV)'),
    ('Voltage_CH1_FullWaveform', 'Highest Voltage Across Full Waveform for CH1 (mV)'),
    ('Voltage_CH2', 'Height of CH2 Pulse (mV)'),
    ('Voltage_CH2_FullWaveform', 'Highest Voltage Across Full Waveform for CH2 (mV)'),
    ('Voltage_CH3', 'Height of CH3 Pulse (mV)'),
    ('Voltage_CH3_FullWaveform', 'Highest Voltage Across Full Waveform for CH3 (mV)'),
    ('Voltage_CH4', 'Height of CH4 Pulse (mV)'),
    ('Voltage_CH4_FullWaveform', 'Highest Voltage Across Full Waveform for CH4 (mV)'),
    ('Voltage_General', 'Height of Pulse (mV)'),
]




#########################################################################################
############## For use in the plot.py model - variable choices for the cuts #############
#########################################################################################

CUT_VAR_CHOICES = [ # TODO: Update variable choices - standardize the naming and fix the units, remove duplicates
    ('none', 'None'),
    ('RunNumber', 'Run Number'),
    ('EventNumber', 'Event Number'),
    ('TotalArea', 'Total Area of Pulse (nVs)'),  # TODO: check description is correct 
    ('Area_CH1', 'Area of CH1 Pulse (nVs)'),
    ('AreaFrac_CH1', 'Fraction of Total Area for CH1'),  # TODO: check description is correct
    ('Voltage_CH1', 'Height of CH1 Pulse (mV)'),
    ('PulseWidth_CH1', 'Width (Duration) of CH1 Pulse (ns)'),  # TODO: check description is correct
    ('PulseTime_CH1', 'Approximate Time of CH1 Pulse'),
    ('LeadingEdgeStartTime_CH1', 'Fitted Start Time of Leading Edge for CH1 Pulse'),
    ('FitPointsCount_CH1', 'Number of Samples Used in Leading Edge Fit for CH1'),  # TODO: check description is correct
    ('FitProb_CH1', 'Chi-squared Probability of Leading Edge Fit for CH1'),
    ('RiseSlope_CH1', 'Rise Slope for CH1 Pulse'),  # TODO: check description is correct
    ('Area_CH2', 'Area of CH2 Pulse (nVs)'),
    ('AreaFrac_CH2', 'Fraction of Total Area for CH2'),  # TODO: check description is correct
    ('Voltage_CH2', 'Height of CH2 Pulse (mV)'),
    ('PulseWidth_CH2', 'Width (Duration) of CH2 Pulse (ns)'),  # TODO: check description is correct
    ('PulseTime_CH2', 'Approximate Time of CH2 Pulse'),
    ('LeadingEdgeStartTime_CH2', 'Fitted Start Time of Leading Edge for CH2 Pulse'),
    ('FitPointsCount_CH2', 'Number of Samples Used in Leading Edge Fit for CH2'),  # TODO: check description is correct
    ('FitProb_CH2', 'Chi-squared Probability of Leading Edge Fit for CH2'),
    ('RiseSlope_CH2', 'Rise Slope for CH2 Pulse'),  # TODO: check description is correct
    ('Area_CH3', 'Area of CH3 Pulse (nVs)'),
    ('AreaFrac_CH3', 'Fraction of Total Area for CH3'),  # TODO: check description is correct
    ('Voltage_CH3', 'Height of CH3 Pulse (mV)'),
    ('PulseWidth_CH3', 'Width (Duration) of CH3 Pulse (ns)'),  # TODO: check description is correct
    ('PulseTime_CH3', 'Approximate Time of CH3 Pulse'),
    ('LeadingEdgeStartTime_CH3', 'Fitted Start Time of Leading Edge for CH3 Pulse'),
    ('FitPointsCount_CH3', 'Number of Samples Used in Leading Edge Fit for CH3'),  # TODO: check description is correct
    ('FitProb_CH3', 'Chi-squared Probability of Leading Edge Fit for CH3'),
    ('RiseSlope_CH3', 'Rise Slope for CH3 Pulse'),  # TODO: check description is correct
    ('Area_CH4', 'Area of CH4 Pulse (nVs)'),
    ('AreaFrac_CH4', 'Fraction of Total Area for CH4'),  # TODO: check description is correct
    ('Voltage_CH4', 'Height of CH4 Pulse (mV)'),
    ('PulseWidth_CH4', 'Width (Duration) of CH4 Pulse (ns)'),  # TODO: check description is correct
    ('PulseTime_CH4', 'Approximate Time of CH4 Pulse'),
    ('LeadingEdgeStartTime_CH4', 'Fitted Start Time of Leading Edge for CH4 Pulse'),
    ('FitPointsCount_CH4', 'Number of Samples Used in Leading Edge Fit for CH4'),  # TODO: check description is correct
    ('FitProb_CH4', 'Chi-squared Probability of Leading Edge Fit for CH4'),
    ('RiseSlope_CH4', 'Rise Slope for CH4 Pulse'),  # TODO: check description is correct
    ('RMSNoise_CH1', 'RMS Noise Measured in Channel1'),
    ('RMSNoise_CH2', 'RMS Noise Measured in Channel2'),
    ('RMSNoise_CH3', 'RMS Noise Measured in Channel3'),
    ('RMSNoise_CH4', 'RMS Noise Measured in Channel4')
]