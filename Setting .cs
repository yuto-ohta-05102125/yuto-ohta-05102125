using UnityEngine;
using Microsoft.MixedReality.Toolkit.UI;
using Microsoft.MixedReality.Toolkit.Input;

[RequireComponent(typeof(MeshCollider))]
[RequireComponent(typeof(ObjectManipulator))]
[RequireComponent(typeof(NearInteractionGrabbable))]

public class Setting : MonoBehaviour
{
    private MeshCollider meshCollider;
    private ObjectManipulator objectManipulator;
    private NearInteractionGrabbable nearGrabbable;
    private Renderer meshRenderer;

    private void Start()
    {
        // MeshColliderコンポーネントを取得する
        meshCollider = GetComponent<MeshCollider>();

        if (meshCollider == null)
        {
            // MeshColliderがアタッチされていない場合は、警告を表示する
            Debug.LogWarning("MeshColliderがアタッチされていません。");
            return;
        }

        // Convexを有効にする
        meshCollider.convex = true;

        // ObjectManipulatorコンポーネントを取得する
        objectManipulator = GetComponent<ObjectManipulator>();

        if (objectManipulator == null)
        {
            // ObjectManipulatorがアタッチされていない場合は、警告を表示する
            Debug.LogWarning("ObjectManipulatorがアタッチされていません。");
            return;
        }

        // ObjectManipulatorを有効にする
        objectManipulator.enabled = true;

        // NearInteractionGrabbableコンポーネントを取得する
        nearGrabbable = GetComponent<NearInteractionGrabbable>();

        if (nearGrabbable == null)
        {
            // NearInteractionGrabbableがアタッチされていない場合は、警告を表示する
            Debug.LogWarning("NearInteractionGrabbableがアタッチされていません。");
            return;
        }

        // NearInteractionGrabbableを有効にする
        nearGrabbable.enabled = true;

        // Rendererコンポーネントを取得する
        meshRenderer = GetComponent<Renderer>();

        if (meshRenderer == null)
        {
            // Rendererがアタッチされていない場合は、警告を表示する
            Debug.LogWarning("Rendererがアタッチされていません。");
            return;
        }

        // モデルのマテリアルを取得する
        Material material = meshRenderer.material;

        // マテリアルの色を緑色に変更する
        material.color = Color.green;

        // 位置を(0,0,1)に移動する
        transform.position = new Vector3(0, 0, 1);
    }
}
