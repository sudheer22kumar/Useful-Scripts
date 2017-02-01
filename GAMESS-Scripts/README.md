GAMESS-Input-Modifier-and-Generator.

NOTE: Inorder to use this script's full potential working GAMESS executable should be present and the path to that executables should be known.

This script has a very specific set of tasks.

Tasks:
1.  To displace any given group of atoms by a given interval/distance any number of times. NOTE: For this to work the input file containing these atoms should be in x,y,z coordinate format.

2.  Each displacement will be recorded as a new input for GAMESS calculation and consequently a new input file will be generated each time with appropriate naming based on the displacement.

3.  Generate a paralled job submission PBS script.
    a.  (NOTE: This is very important) If GAMESS is installed and the script is configured with the corresponding path of the executables, then the script automatically runs the GAMESS jobs using PBS script.
    b.  Hence, if job submission is different from PBS then this part of the code must be modified.

4.  Generate a perl script called "Extract_Log_.*" serving the purpose of extracting information from the output files from GAMESS job submission for example Energies corresponding to each displacement and such. The files being generated are self-explanatory once a successful execution of this program is achieved.

