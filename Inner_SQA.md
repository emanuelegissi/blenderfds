# Software quality assurance #


---


Software quality assurance is defined as a systematic approach to the evaluation of the quality of and adherence to software standards, processes, and procedures.

Each BlenderFDS release is fully verified by running the export algorithm against the test suite case. The test suite contains all BlenderFDS features.
The resulting input file is compared (`diff`) to those obtained by previous releases.

The code contains specific tools to verify the performance of the voxelization and boxelization algorithms. This tools are run after each code modification.

Code quality, readability and maintainability is preferred over new features.