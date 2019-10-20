## General notes about satellite
- Magnetometer failed due to coarse sensor
-- Sol'n: Signal pattern from GPS + direction of own GPS antennae ==> can determine own orientation
- Torque rod failue results in loss of control / pointing
-- Sol'n: Satellite's own magnetic dipole interacts with Earth's magnetic field, resulting in torque rod.

## Metadata
 - Stored in ASCII readable header
 - Link for cleaning code: https://github.com/jasonfrowe/neossat

 - Folder structure
 - - first folder: Year(2019, 2018, ...)
 - - Second folder: Day(1, 2, ...)

 - Raw Images: NEOS_SCI_YYYYDDDHHMMSS.fits
 - Java overscan cleaning: NEOS_SCI_YYYYDDDHHMMSS_clean.fits
 - Python overscan cleaning: NEOS_SCI_YYYYDDDHHMMSS_cor.fits
 - Python overscan+dark cleaning: NEOS_SCI_YYYYDDDHHMMSS_cord.fits

 - 'Seeing Space' of an image is 1024 x 1024 w/ 16, 3 dark pixels on top, bottom respectively.
 - - FOV w/in 1024 x 1024 = .86 degrees, or about 3 arc-seconds
 - -  Origin @ centre
 - Total images are 1072 x 1072, due to blank overscan taking up the rest

 - Keyword name is uppercase and fits in first 8 bytes (bytes 1 to 8) (and is padded with spaces to be 8 bytes long). Note that in some case we use leading zeros for indices, which is specifically forbidden in the FITS standard (e.g. CCDCLK01 instead of CCDCLK1).
 - When a value follows, next two bytes (bytes 9 and 10) are “= “ (equal sign plus a space);
 - Remaining bytes (11 to 80) contains the value in ASCII text and a comment preceeded by “/”.

## Datapoints Definitions:
| METADATA CATEGORY | DATAPOINT              | DESCRIPTION                                                                                                       |
|-------------------|------------------------|-------------------------------------------------------------------------------------------------------------------|
| ----------------- |  --------              | -----------                                                                                                       |
| IMAGE             | EXPOSURE               | Length of exposure.                                                                                               |
|                   | AExptime               | Actual exposure length.                                                                                           |
|                   | Date/Time-Obs          | Date/Time of observation (YYYYMM-DDTHH-MM:SS:ss).                                                                 |
|                   | R/A-Exposure           | requested / actual start time of exposure (2 different rows).                                                     |
| POINTING          | CMD                    | Commanded spacecraft pointing (Celestial Coordinates).                                                            |
|                   | ELA min/maxk           | Earth limb angle.                                                                                                 |
|                   | Vel_nnn                | Velocity around X/Y/Z.                                                                                            |
|                   | Roll / Avg / Dec_VEL   | Roll, Avg, Declination velocity @ midpoint of exposure.                                                           |
| ENVIRO            | P/N # V: P = +-, V = # | supply sensor reading.                                                                                            |
|                   | CCDBIAS (0-7)          | Voltage for CCD clocking line.                                                                                    |
| MPS               | OBJECT                 | Prime Object Name.                                                                                                |
|                   | OBSERVER               | HEOSS // NESS // Astro (Satellite, specified by user).                                                            |
|                   | EPOSi-j                | ECEF Position @ Exposure start / middle / end (X, Y, Z).                                                          |
|                   | EVEL                   | ECEF Velocity @ Exposure start / middle / end (X, Y, Z).                                                          |
|                   | JPOS                   | J2000 Position @ Exposure start / middle / end (X, Y, Z).                                                         |
|                   | JVEL                   | J2000 Velocity @ Exposure start / middle / end (X, Y, Z).                                                         |
| MPS               | META_XXX               | "OK" if metadata of XXX is present, "MISSING" otherwise.                                                          |
|                   | IMGSTATE               | Indicates if data received + decoded is complete. "NOT_VERIFIED", "INCOMPLETE", "COMPLETE", "HAS_ZEROES".         |
|                   | IMG_PERC               | The percentage of completion of the image. < 100% ==> some pixel values lost during delivery process or decoding. |

## Raw Data Description (Not in Tables)

SIMPLE
String
Set to True (“T”), must be first record for standard FITS
BITPIX
bits
Bits per pixel for image data. Set to 16 in our case
NAXIS
Axis
Number of axis in the represented image. Our image is a 2-D CCD plane, so this value is set to 2
NAXIS1
Pixels
Size of image – Xaxis, in units of pixels. Note that in our case, depending on the read list, an “image” may be a mosaic of several sub-images from an exposure. NAXIS1 and NAXIS2 provide the outside boundary of a composite image containing all sub-images
NAXIS2
Pixels
Size of image – Yaxis, in units of pixels. See NAXIS1 for more details
BSCALE
Factor
Data scaling. Set to ‘1’
BZERO
Adu
zero def of pixel (for unsigned short). Set to 32768 

IMAGE

BIASSEC
Pixel range
Overscan area, in image coordinates [colStart:colEnd,rowSt,rowEnd]
TRIMSEC
Pixel range
Science area, in image coordinates [colStart:colEnd,rowSt,rowEnd]
DATASEC
Pixel range
Science area, in image coordinates [colStart:colEnd,rowSt,rowEnd]
CCDSEC
Pixel range
Science data coordinates in CCD system [colStart:colEnd,rowSt,rowEnd]. Per image coordinate conventions, indices start at 1, not zero.
CORNER1X
Column
Image coordinates in CCD system, lower left corner column. Indices starts at zero, and may be negative to include overscan. See section “Image Coordinates” for more details
CORNER1Y
Row
Image coord in CCD system, Lower Left Corner row
CORNER2X
Column
Image coord in CCD system, Upper Right Corner column
CORNER2Y
Row
Image coord in CCD system, Upper Right Corner row
OPAMP
String
Read out chain used: Left, right, both. Note that if this image is composed of sub-images, individual sub-images could have different OPAMP settings. Individual OPAMP settings are not provided in the FITS header.
GAIN
String
Estimated CCD amplifier gain in electrons per analog unit. When OPAMP String equals “both”, two comma-separate values are specified (GAIN_LEFT, GAIN_RIGHT).
RDNOISE
String
Estimated CCD readout noise in electrons. When OPAMP String equals “both”, two comma-separate values are specified (RDNOISE_LEFT, RDNOISE_RIGHT). If binning is in effect, multiply the RDNOISE by the binning factor, as binning is implemented on the CCD as a hardware summation of the contributing pixels, (charge from group of pixel cells dumped into the accumulators for the row/column).
XBINNING
Pixels
Number of grouped CCD pixels, on the X-axis (binning, X)
YBINNING
Pixels
Number of grouped CCD pixels, on the Y-axis (binnin, Y)
COMPR_AL
String
Identification of the algorithm used for compressing image data (by the spacecraft), or “Uncompress” if compression was not used.
COMP_SET
Integer
Compression settings, as reported by the spacecraft. For now, only value ‘1’ is expected, as there is only one possible setting. If image is not compressed, this record will specify “N/A”.
N_SUBIMG
Counter
Number of sub-images composing this image. Note that if there is only one main image, this record will be set to zero. If there are sub-images, there will be at least two of them, so this record possible values are 0, then 2 to the maximum number of sub-images. Coordinates of every sub-images are given in subsequent fields, with first sub-image identified as sub-image zero. Note that the maximum number of sub-images is 10.
RGNnnnX1
Column
Sub-image nnn (starting at zero) , x position of bottom left corner in CCD coordinate system.
RGNnnnY1
Row
Sub-image nnn (starting at zero) , y position of bottom left corner in CCD coordinate system.
RGNnnnX2
Column
Sub-image nnn (starting at zero) , x position of top right corner in CCD coordinate system.
RGNnnnY2
Row
Sub-image nnn (starting at zero) , y position of top right corner in CCD coordinate system.
OVERSCAN
Flag
Indicates whether this image contains overscan pixel values (lying outside of the CCD area, therefore not corresponding to actual CCD pixels). Possible values are zero (for NO) and non-zero (for OVERSCAN DATA present). Note that the standard overscan columns on the edge of the CCD chip are not counted as ‘overscan’ per se.
CREATOR
String
Origin of FITS file. Fixed to “NEOSSat”.
TELESCOP
String
Identification of the telescope used to take the image. Fixed to “NEOSSat”.
SHUTTER
String
Shutter status (OPEN or CLOSED). The reported status number is given, followed by a description string (e.g. ‘0 (open)’). Dark frame images for NEOSSat are specified by the shutter being closed.
SHUT_AGE
Seconds
Specifies the time elapsed since the SHUTTER state is in effect. Note that a negative number represents time in the past (which will normally be the case).
DETECTOR
String
Identification of the detector being used (Science or Star Tracker) to generate this image. 


TIMING Placeholder for timing specification header


TIMESYS
String
Time scale specification (set to ‘UTC’)
EXPOSURE
Seconds
Actual Length of exposure
AEXPTIME
Seconds
Actual length of exposure. This record is identical to EXPOSURE, and was added because needed by MPS using this particular keyword.
REXPTIME
Seconds
Requested length of exposure.
DATE-OBS
Date & Time
Date of observation (start of exposure). Format is YYYY-MM-DDTHH:MM:SS.sss.
TIME-OBS
Date & Time
Time of observation (start of exposure). Format is YY-MM-DDTHH:MM:SS.sss.
JD-OBS
JD
Date of observation (start of exposure). Expressed in Julian Date (continuous count of days since noon Universal Time on Jan 1st, 4713 BCE on the Julian calendar).
R_EXP_S
Date & Time
Requested exposure start time. Format is YY-MM-DDTHH:MM:SS.sss. Note that the actual exposure start time may differ from the commanded one.
A_EXP_S
Date & Time
Actual exposure start time. Format is YYYY-MM-DDTHH:MM:SS.sss. This is a duplicate of record DATE-OBS, required by MPS.
LEN_FLU
Seconds
Length of the CCD FLUSH operation in the process of taking this image.
LEN_TRAN
Seconds
Length of the frame transfer operation in the process of taking this image.
LEN_READ
Seconds
Length of the frame transfer and readout operations in the process of taking this image.
LEN_PROC
Seconds
Length of post-processing operations in the process of taking this image.
LENDELAY
Seconds
Length of the delay between exposure command execution and the first operation (CCD FLUSH) involved in taking this image. 


POINTING Placeholder for pointing specification header


EQUINOX
Year
Equatorial coordinates. Fixed to 2000.0 (for J2000)
MODE
String
Spacecraft Attitude Control System (ACS) pointing state. The number (as specified in the spacecraft ACS state diagram) is given, followed by a string identifying the mode. The key imaging modes for NEOSSat are:
16-FINE_POINT : indicates NEOSSat is stabilized relative to fixed stars
14-FINE_SLEW : indicates NEOSSat is slewing to track a moving object. The slew rate can be determined using RA_VEL, DEC_VEL, ROL_VEL.
Dark frame images (taken with the shutter closed) typically cannot be taken in these modes and so mode should be ignored on those cases. Non-dark images that are in neither FINE_POINT nor FINE_SLEW are typically not useful for science purposes.
MODETIME
Seconds
Time elapsed since the spacecraft entered the specified MODE. This number, expressed in seconds, will always be negative as it represents time in the past.
CMD
Radians
Commanded spacecraft pointing, celestial coordinates, in Science CCD frame. Format = ‘RA=x.xxx DEC=x.xxx ROLL=x.xxx’
CMDRA
hrs,min,sec
Commanded Right Acension (RA), in Science CCD frame. Format is ‘hh mm ss.s’ where hh=hours, mm=minutes and ss.s=decimal seconds
CMDDEC
deg,min,sec
Commanded Declination (DEC) , in Science CCD frame. Format is ‘dd mm ss.s’ where dd=degrees, mm=minutes and ss.s=decimal seconds
CMDROL
Degrees
Commanded Roll, in degrees, in Science CCD frame.
CMDQ0
n/a
Commanded quaternion qp[0]. Represents QB, or “i” in the “scalar,i,j,k” notation.
CMDQ1
n/a
Commanded quaternion qp[1]. Represents QC, or “j”.
CMDQ2
n/a
Commanded quaternion qp[2]. Represents QD, or “k”.
CMDQ3
n/a
Commanded quaternion qp[3]. Represents QA, or “scalar”.
OBJCTRA
hrs,min,sec
Actual Right Ascension (RA) at start of exposure, in Science CCD frame. Format is ‘hh mm ss.s’ where hh=hours, mm=minutes and ss.s=decimal seconds.
OBJCTDEC
deg,min,sec
Actual Declination (DEC) at start of exposure, in Science CCD frame. Format is ‘dd mm ss.s’ where dd=degrees, mm=minutes and ss.s=decimal seconds.
OBJCTROL
degrees
Actual Roll at start of exposure, in Science CCD frame, provided in degrees.
RA
hrs:min:sec
Actual Right Ascension (RA). Same as OBJCTRA using ‘hh:mm:ss.s’ format, where hh=hours, mm=minutes and ss.s=decimal seconds.
DEC
deg:min:sec
Actual Declination (DEC). Same as OBJCTDEC using ‘dd:mm:ss.s’ format, where dd=degrees, mm=minutes and ss.s=decimal seconds.
ELA_MIN
degrees
Minimum Earth limb angle attained while exposing, from an axis perpendicular to the image plane.
ELA_MAX
degrees
Maximum Earth limb angle attained while exposing, from an axis perpendicular to the image plane.
ELA_ANG
degrees
Angle to Earth Limb while exposing. NOTE that at this moment we populate this record with ELA_MIN value. It is TBC if this is adequate.
SUN_MIN
degrees
Minimum Sun angle attained while exposing, from an axis perpendicular to the image plane.
SUN_MAX
degrees
Maximum Sun angle attained while exposing, from an axis perpendicular to the image plane.
HIST_NB
count
Number of ACS history points (i.e. number of samples of pointing data recorded and provided while exposing) that follows this field. Note that whenever Star Tracker is operating (e.g. in fine pointing modes), the ACS history will contain data exclusively computed from Star Tracker solutions, and provided at the same rate as Star Tracker images (typically between 0.5 and 1Hz). When Star Tracker is not operating, estimated EKF data at full rate (5Hz) is provided.
DELT_nnn
seconds
Time difference between this pointing data sample (identified by a sequence number nnn starting at 000) and the start of exposure. The first sample can be before the actual exposure start, represented by a negative number here. This is part of the ACS history.
DEV_nnn
arc-sec
A sample of the spacecraft pointing wander while exposing. Expressed in rotations around X/Y/Z body frame axis, relative to the first attitude data point (therefore DEV_000 will always be “0 0 0”). . This is part of the ACS history.
VEL_nnn
rad/sec
A sample of the spacecraft estimated velocity. Expressed around X/Y/Z body frame axis at instantaneous time. This is part of the ACS history.
AVG_VEL
arcsec/s
Average angular slew velocity in the body frame
RA_VEL
hours/s
Signed angular slew velocity in Right Ascension (RA) at midpoint of the exposure.
DEC_VEL
degrees/s
Signed angular slew velocity in Declination at midpoint of the exposure.
ROL_VEL
degrees/s
Signed angular slew velocity in Roll at midpoint of the exposure. 

ENVIRO Placeholder for environment data header


TEMP_CCD
kelvins
Temperature of CCD. If the CCD temperature history is available, the temperature will be the average of all temperature samples taken while exposing (+/- 1 second). If the CCD temperature history is not available, this value is set from the temperature sample sent by the imager after readout (which will be several seconds after exposure, more than 30 seconds for a full image).
CCD-TEMP
Celsius
Temperature of CCD in Celsius. Derived from the value of TEMP_CCD, using formula CCD-TEMP = TEMP_CCD – 273.15.
CCDT_NB
Count
Number of samples included in the CCD temperature history, that follows this field.
CCDT_nnn
Various
Provides data related to a specific sample of the CCD temperature history, in addition to the state of the transmitters.
Format = ‘S.SSS KKK.K TX- TX+’ where
S.SSS = Number of seconds between this sample and start of exposure (negative if prior exposure).
KKK.K = Temperature of the CCD in Kelvins.
TX- = “ON” if minus_Y transmitter module is powered ON, ”OFF” if powered OFF, ”N/A” if status is unknown.
TX+ = Same as TX-.
NOTE THAT a module being powered ON does not necessarily mean that data transmission is underway.
Example: ’71.302 230.5 OFF OFF’means that this sample was taken 71.302 seconds after start of exposure, the CCD was at 230.5K, and both transmitters were OFF. Note that when this CCD temperature history is available, all temperature with a number of seconds from exposure between -1 and +(exposure time+1) are retained and averaged to produce the TEMP_CCD value.
TEMP_ROE
kelvins
Temperature of the imager (Read-Out Electronics or ROE) after image exposure and readout.
TEMP_AMP
kelvins
Temperature of the pre-amplifier electronics after image exposure and readout.
TEMP_PLD
kelvins
Temperature of the imager (ROE) Programmable Logic Device circuit (FPGA) after image exposure and readout.
P28V
volts
+28V supply sensor reading.
P24V
volts
+24V supply sensor reading.
P12V
volts
+12V supply sensor reading.
N12V
volts
-12V supply sensor reading.
P10V
volts
+10V supply sensor reading.
N10V
volts
-10V supply sensor reading.
P5V
volts
+5V supply sensor reading.
N5V
volts
-5V supply sensor reading.
P5VD
volts
+5V differential supply sensor reading.
P3V3D
volts
+3.3V supply sensor reading.
vTG
volts
TG voltage reading.
CCDBIAS0
volts
Voltage for CCD clocking line - IMG_L_BIAS
CCDBIAS1
volts
Voltage for CCD clocking line - IMG_R_BIAS
CCDBIAS2
volts
Voltage for CCD clocking line - ODR
CCDBIAS3
volts
Voltage for CCD clocking line - ODL
CCDBIAS4
volts
Voltage for CCD clocking line - RDR
CCDBIAS5
volts
Voltage for CCD clocking line - RDL
CCDBIAS6
volts
Voltage for CCD clocking line - OG
CCDBIAS7
volts
Voltage for CCD clocking line – ABG
CCDCLK00
volts
Voltage for CCD clocking line - IPC-
CCDCLK01
volts
Voltage for CCD clocking line - IPC+
CCDCLK02
volts
Voltage for CCD clocking line - RG-
CCDCLK03
volts
Voltage for CCD clocking line - RG+
CCDCLK04
volts
Voltage for CCD clocking line - S- R1L/R2L/R3L
CCDCLK05
volts
Voltage for CCD clocking line - S+ R1R/R2R/R3R
CCDCLK06
volts
Voltage for CCD clocking line - DG-
CCDCLK07
volts
Voltage for CCD clocking line - DG+
CCDCLK08
volts
Voltage for CCD clocking line - TG-
CCDCLK09
volts
Voltage for CCD clocking line - TG+
CCDCLK10
volts
Voltage for CCD clocking line - P1- ST1-/IM1-
CCDCLK11
volts
Voltage for CCD clocking line - P1+ ST1+/IM1+
CCDCLK12
volts
Voltage for CCD clocking line - P2- ST2-/IM2-
CCDCLK13
volts
Voltage for CCD clocking line - P2+ ST2+/IM2+
CCDCLK14
volts
Voltage for CCD clocking line - P3- ST3-/IM3-
CCDCLK15
volts
Voltage for CCD clocking line - P3+ ST3+/IM3+ 

MPS Placeholder for the MPS section header


OBJECT
String
Prime object name (specified by the user)
OBSERVER
String
HEOSS || NESS || ASTRO (specified by the user)
M1
Tbd
Future Use
M2
String
State Vector Solution Status, specifying the source of the state vector data (from GPS telemetry or .navsol). Currently one of three Status’: FINE_TLM_T, FINE_NAVSOL_T, NO_SOLUTION_T, where ‘T’ represents the largest timestep, in seconds, between GPS data points used for interpolation of solution. (T < 5 indicate nominal GPS data availability)
EPOS1_1
km
ECEF Position at Exp start, X-component
EPOS1_2
km
ECEF Position at Exp start, Y-Component
EPOS1_3
km
ECEF Position at Exp start, Z-Component
EPOS2_1
km
ECEF Position at Exp middle, X-component
EPOS2_2
km
ECEF Position at Exp middle, Y-component
EPOS2_3
km
ECEF Position at Exp middle, Z-component
EPOS3_1
km
ECEF Position at Exp end, X-component
EPOS3_2
km
ECEF Position at Exp end, Y-component
EPOS3_3
km
ECEF Position at Exp end, Z-component
JPOS1_1
km
J2000 Position at Exp start, X-component
JPOS1_2
km
J2000 Position at Exp start, Y-component
JPOS1_3
km
J2000 Position at Exp start, Y-component
JVEL1_1
km/s
J2000 Velocity at Exp start, X-component
JVEL1_2
km/s
J2000 Velocity at Exp start, Y-component
JVEL1_3
km/s
J2000 Velocity at Exp start, Z-component
JPOS2_1
km
J2000 Position at Exp middle, X-component
JPOS2_2
km
J2000 Position at Exp middle, Y-component
JPOS2_3
km
J2000 Position at Exp middle, Z-component
JVEL2_1
km/s
J2000 Velocity at Exp middle, X-component
JVEL2_2
km/s
J2000 Velocity at Exp middle, Y-component
JVEL2_3
km/s
J2000 Velocity at Exp middle, Z-component
JPOS3_1
km
J2000 Position at Exp end, X-component
JPOS3_2
km
J2000 Position at Exp end, Y-component
JPOS3_3
km
J2000 Position at Exp end, Z-component
JVEL3_1
km/s
J2000 Velocity at Exp end, X-component
JVEL3_2
km/s
J2000 Velocity at Exp end, Y-component
JVEL3_3
km/s
J2000 Velocity at Exp end, Z-component
EVEL3_1
km/s
ECEF Velocity at Exp end, X-component
EVEL3_2
km/s
ECEF Velocity at Exp end, Y-component
EVEL3_3
km/s
ECEF Velocity at Exp end, Z-component
EVEL2_1
km/s
ECEF Velocity at Exp middle, X-component
EVEL2_2
km/s
ECEF Velocity at Exp middle, Y-component
EVEL2_3
km/s
ECEF Velocity at Exp middle, Z-component
EVEL1_1
km/s
ECEF Velocity at Exp start, X-component
EVEL1_2
km/s
ECEF Velocity at Exp start, Y-component
EVEL1_3
km/s
ECEF Velocity at Exp start, Z-component 

DIAG Placeholder for diagnostic section header

ROE_SW
String
Identification of the imager (Read-Out Electronics or “ROE”) software version running at the time the image was taken.
S921_SW
String
Identification of the C&DH flight software version running at the time the image was taken.
CONV_SW
String
Identification of the version of the ground software used to convert raw science data into this FITS image (FITS Processor version).
TMFILEn
String
n=0..00. Provides name of source telemetry file. As data for an image can be contained in multiple telemetry files (usually no more than 2 consecutive files), the name of each one is given here (e.g. ‘TMFILE0='NEOS_20141852225H.VC1', ‘TMFILE1='NEOS_20141852355H.VC1')
META_TLM
String
Indicates if image telemetry meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 TEMP_AMP, TEMP_CCD, TEMP_ROE
 P28V, P24V… TG_sense
META_TIM
String
Indicates if image timing meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 EXPOSURE, AEXPTIME
 LENDELAY, LEN_FLU, LEN_TRAN, LEN_READ, LEN_PROC
 R_EXP_S, A_EXP_S
 TIME_OBS, DATE_OBS, JD_OBS
META_ACS
String
Indicates if ACS history meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 HIST_NB
 MODE
 CMD
 CMDRA, CMDDEC, CMDROL
 CMDQ0 to CMDQ3
 MINEARTH, MAXEARTH
 MINSUN, MAXSUN
 OBJRA, OBJDEC, OBJROL
 SHUTTER
 Wander data
META_CCD
String
Indicates if CCD history meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 CCDT_NB
 CCD history data (including TX state)
Note also that if META_CCD is MISSING, the value of field TEMP_CCD will be that of TEMP_CCD returned by META_TLM, which is a sample taken several seconds after exposure (less accurate), instead of being calculated from an average of CCD temperature history during exposure.
META_VLT
String
Indicates if voltages meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 CCDBIAS0..7
 CCDCLK0..15
 CCDBIAS0_IMG_L_BIAS_RAW
 …
 CCDCLK15_P3P_ST3P_IM3P_RAW
META_FSW
String
Indicates if SW Versions meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled:
 S921_SW
 ROE_SW
META_RDL
String
Indicates if image read list meta-data packet was accompanying this image. Possible values are “OK” or “MISSING”. If missing, some records in the header won’t be filled or will be filled with default values not necessarily corresponding to actual image specifications:
 NAXIS1, NAXIS2
 OPAMP
 GAIN
 XBINNING, YBINNING
 NYSCAN
 CORNER1_X, CORNER2_X, CORNER1_Y, CORNER2_Y
and the decoding software will not be able to determine the specification of the image (i.e. size, coordinates, sub-rasters...) so there is a high probability that the image displayed with be incoherent.
IMGSTATE
String
An indication if the data received from the spacecrafted and decoded is complete for this image. Possible values are ‘NOT_VERIFIED’, ‘INCOMPLETE’, ‘COMPLETE’ and ‘HAS_ZEROS’, where:
NOT_VERIFIED = The FITS processor was not able to determine the state of the image (not a nominal case).
INCOMPLETE = Not all expected pixel values for this image were extracted from telemetry. There will be missing data within the image.
COMPLETE = All expected data have been read and used to create the image. There are no pixel value that have been seen at value zero.
HAS_ZEROS = All expected data have been read, however some pixel have zero values, which is not a nominal case for images taken with the spacecraft.
IMG_PERC
0-100%
Percentage of completion of the image (i.e. number of pixels read from telemetry vs total number of pixels needed to complete the image). A value of less than 100% means that some pixel values were ‘lost’ in the delivery process from space or decoding. Note that this percentage does not include image meta-data.
NB_0_PIX
Nb pixels
Number of pixel that have exactly the value 0 (or black pixel). Note that a value different than zero indicates a non-nominal situation, except for specific test images taken on the flatsat.
FRM_SEQ
String
Indicates whether raw telemetry transfer frame sequence (Virtual Channel Counter), while dumping this image, was continuous or not. Possible values are “OK” or “n ANOMALIES” where n gives the number of “holes” in the sequence. These anomalies would be signatures for downlink problems. If anomalies, we can expect that some pixel data
will be missing (see IMGSTATE and IMG_PERC). The application will not detected missing frame at the beginning or at the end of the image.
PKT_SEQ
String
Indicates whether raw telemetry packet sequence counter, while dumping this image from the spacecraft, was continuous or not. Possible values are “OK” or “n ANOMALIES” where n gives the number of “holes” in the sequence. These anomalies would be signatures for downlink problems. If anomalies, we can expect that some pixel data will be missing (see IMGSTATE and IMG_PERC). The application will not detected missing frame at the beginning or at the end of the image. EXTEND Set at value “T” to specify extension HDU exists
END
N/A
Specifies the end of the primary header