| **Updated to 2.0** |
|:-------------------|

Before you begin modeling always remember that, when you are modeling a Blender `object` that needs to be _voxelized_, it is better to create a volume that make sense in a physical world: _water-tight_ and _well-formed_ so that BlenderFDS can decide which portion of space is solid and which is instead void.

The easiest way to do this is to work by extruding existing volume, and using boolean operations to combine volumes. It is often difficult to retrofit existing models, so it is best to start from scratch and with each step keep the goal in mind. Models made for visualization are often not good for voxelization.




---


# Fixing non-manifold models #

| **New in 2.0**: The new voxelization algorithm can treat both _manifold_ and _non-manifold_ objects |
|:----------------------------------------------------------------------------------------------------|

The new voxelization algorithm can treat both _manifold_ and _non-manifold_ objects, but exported geometries are more precise if their originating objects are _manifold_, that is water-tight and well-formed, so that BlenderFDS can decide which portion of space is solid and which is instead void. This is the reason why, if the object is non-manifold, a warning message is displayed.

We share this problem with people working in 3D printing processes. One of the best and detailed explications of the problem and how to fix it is found on Shapeways site: [Fixing non-manifold models](http://www.shapeways.com/tutorials/fixing-non-manifold-models)

The suggested operations can be performed directly inside Blender (Shapeways folks use Blender, too!).

When desperate there is another powerful but somewhat more complex tool: [MeshLab](http://meshlab.sourceforge.net/). You need to export your `object mesh` from Blender in STL format, fix it in MeshLab, and import it back into Blender: a procedure not meant for the faint of hearth...

Remember that it is often quicker to remodel the problematic `object` from scratch.

# An example: how to fix a non-manifold object #

The following picture shows a rotated cube. The cube lacks one face, and is thus non-manifold. If the user tries to set `XB` to `Voxels`, a warning message appears in the `object properties panel`:

![https://lh5.googleusercontent.com/-F8HAZ2MsQIA/UDssNcz0wUI/AAAAAAAAAtE/w7JossOuMlQ/s800/m1.png](https://lh5.googleusercontent.com/-F8HAZ2MsQIA/UDssNcz0wUI/AAAAAAAAAtE/w7JossOuMlQ/s800/m1.png)

To fix it, the user clicks on the `Select Non-Manifold Edges` button. Blender switches from `Object mode` to `Edit mode` and problematic edges are selected:

![https://lh5.googleusercontent.com/-1x-mQPczoXU/UDssNSagsDI/AAAAAAAAAs8/MoGp6ce9GjE/s800/m2.png](https://lh5.googleusercontent.com/-1x-mQPczoXU/UDssNSagsDI/AAAAAAAAAs8/MoGp6ce9GjE/s800/m2.png)

It is often better to first delete problematic vertices, edges, and faces, then rebuild them properly, especially if they are deeply hidden inside a complex solid. But in this simple case the user can just fill the missing face by pressing the `f` key:

![https://lh4.googleusercontent.com/-Sd-iBaZiZas/UDssNZWntoI/AAAAAAAAAs4/e2FoVxWhKwU/s800/m3.png](https://lh4.googleusercontent.com/-Sd-iBaZiZas/UDssNZWntoI/AAAAAAAAAs4/e2FoVxWhKwU/s800/m3.png)

Then the user switches back to `Object Mode` and the warning message disappears. It is time to check for voxelization quality.

![https://lh3.googleusercontent.com/-yXfpP5pOmuU/UDssN-BIe-I/AAAAAAAAAtI/e5VcVUUa21g/s800/m4.png](https://lh3.googleusercontent.com/-yXfpP5pOmuU/UDssN-BIe-I/AAAAAAAAAtI/e5VcVUUa21g/s800/m4.png)

The user clicks on the `Show Voxels` button and this is what is obtained. The voxelized object seems good:

![https://lh5.googleusercontent.com/-TItAk5AXz-k/UDssOFft2OI/AAAAAAAAAtM/F2n9f6mEHNI/s800/m5.png](https://lh5.googleusercontent.com/-TItAk5AXz-k/UDssOFft2OI/AAAAAAAAAtM/F2n9f6mEHNI/s800/m5.png)

# An example: most non-manifold objects can be correctly voxelized #

As already said, the new voxelization algorithm can treat _non-manifold_ objects. In the previous simple case where one only face was missing, even if the geometry was not fixed, it could produce an as good voxelized object. This would be the result:

![https://lh6.googleusercontent.com/-99ejvn1Nv1U/UDssOwYvcnI/AAAAAAAAAtg/vbZLxhTI1Qc/s800/m8.png](https://lh6.googleusercontent.com/-99ejvn1Nv1U/UDssOwYvcnI/AAAAAAAAAtg/vbZLxhTI1Qc/s800/m8.png)

But if the originating object is badly non-manifold, like the following one where two faces are missing...

![https://lh5.googleusercontent.com/-B5UQN_EYJmM/UDssOZOgm7I/AAAAAAAAAtU/AaECdKYWzso/s800/m6.png](https://lh5.googleusercontent.com/-B5UQN_EYJmM/UDssOZOgm7I/AAAAAAAAAtU/AaECdKYWzso/s800/m6.png)

... the voxelization algorithm cannot produce an as good voxelized object:

![https://lh3.googleusercontent.com/-UthQQNhyhNg/UDssOt_Zv2I/AAAAAAAAAtY/mMB6vd1wmcE/s800/m7.png](https://lh3.googleusercontent.com/-UthQQNhyhNg/UDssOt_Zv2I/AAAAAAAAAtY/mMB6vd1wmcE/s800/m7.png)