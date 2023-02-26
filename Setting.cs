using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class Setting : MonoBehaviour
{
    void Start()
    {
        Renderer rendererComponent = gameObject.GetComponent<Renderer>();
        Material materialComponent = rendererComponent.material;
        materialComponent.color = Color.green;
        
        transform.position = new Vector3(0, 0, 1);
    
        MeshCollider meshCollider = GetComponent<MeshCollider>();
        if (meshCollider != null)
        {
            meshCollider.convex = true;
        }
    }
    [MenuItem("GameObject/Object Manipulator")]
    static void Attach()
    {
        ObjectManipulator manipulator = new ObjectManipulator();
        Selection.activeTransform = manipulator.AttachSelection();
    }
    private XRGrabInteractable grabInteractable;

    private void Awake()
    {
        grabInteractable = GetComponent<XRGrabInteractable>();

        NearInteractionGrabbable nearGrabbable = GetComponent<NearInteractionGrabbable>();

        nearGrabbable.Radius = 0.1f;

        grabInteractable.trackPosition = true;
        grabInteractable.trackRotation = true;
    }

    private void OnEnable()
    {
        grabInteractable.enabled = true;
    }

    private void OnDisable()
    {
        grabInteractable.enabled = false;
    }
}
