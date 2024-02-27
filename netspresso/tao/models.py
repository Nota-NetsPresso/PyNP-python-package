CLASSIFICATION = {
    "multitask_classification": {
        "vgg19": "nvidia/tao/pretrained_classification:vgg19",
        "vgg16": "nvidia/tao/pretrained_classification:vgg16",
        "squeezenet": "nvidia/tao/pretrained_classification:squeezenet",
        "resnet50": "nvidia/tao/pretrained_classification:resnet50",
        "resnet34": "nvidia/tao/pretrained_classification:resnet34",
        "resnet18": "nvidia/tao/pretrained_classification:resnet18",
        "resnet101": "nvidia/tao/pretrained_classification:resnet101",
        "resnet10": "nvidia/tao/pretrained_classification:resnet10",
        "mobilenet_v2": "nvidia/tao/pretrained_classification:mobilenet_v2",
        "mobilenet_v1": "nvidia/tao/pretrained_classification:mobilenet_v1",
        "googlenet": "nvidia/tao/pretrained_classification:googlenet",
        "darknet53": "nvidia/tao/pretrained_classification:darknet53",
        "darknet19": "nvidia/tao/pretrained_classification:darknet19",
        "cspdarknet53": "nvidia/tao/pretrained_classification:cspdarknet53",
        "cspdarknet19": "nvidia/tao/pretrained_classification:cspdarknet19",
    },
    "classification_pyt": {
        "deployable_fastervit_6_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_6_224_1k_op17",
        "deployable_fastervit_5_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_5_224_1k_op17",
        "deployable_fastervit_4_768_21k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_4_768_21k_op17",
        "deployable_fastervit_4_512_21k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_4_512_21k_op17",
        "deployable_fastervit_4_384_21k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_4_384_21k_op17",
        "deployable_fastervit_4_224_21k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_4_224_21k_op17",
        "deployable_fastervit_4_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_4_224_1k_op17",
        "deployable_fastervit_3_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_3_224_1k_op17",
        "deployable_fastervit_2_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_2_224_1k_op17",
        "deployable_fastervit_1_224_1k_op17": "nvidia/tao/pretrained_fastervit_classification_imagenet:deployable_fastervit_1_224_1k_op17",
        "fastervit_0_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_0_224_1k",
        "fastervit_1_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_1_224_1k",
        "fastervit_2_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_2_224_1k",
        "fastervit_3_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_3_224_1k",
        "fastervit_4_21k_224_w14": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_4_21k_224_w14",
        "fastervit_4_21k_384_w24": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_4_21k_384_w24",
        "fastervit_4_21k_512_w32": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_4_21k_512_w32",
        "fastervit_4_21k_768_w48": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_4_21k_768_w48",
        "fastervit_4_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_4_224_1k",
        "fastervit_5_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_5_224_1k",
        "fastervit_6_224_1k": "nvidia/tao/pretrained_fastervit_classification_imagenet:fastervit_6_224_1k",
        "deployable": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:deployable-fastervit-1-nvimagenet_op17",
        "deployable": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:deployable-fastervit-2-nvimagenet_op17",
        "deployable": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:deployable-fastervit-4-nvimagenet_op17",
        "fastervit-1-nvimagenet": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:fastervit-1-nvimagenet",
        "fastervit-2-nvimagenet": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:fastervit-2-nvimagenet",
        "fastervit-4-nvimagenet": "nvidia/tao/pretrained_fastervit_classification_nvimagenet:fastervit-4-nvimagenet",
        "trainable_v1.0": "nvidia/tao/pcb_classification:trainable_v1.0",
        "gcvit_xxtiny_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_xxtiny_imagenet1k",
        "gcvit_xtiny_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_xtiny_imagenet1k",
        "gcvit_tiny_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_tiny_imagenet1k",
        "gcvit_small_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_small_imagenet1k",
        "gcvit_base_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_base_imagenet1k",
        "gcvit_large_imagenet1k": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_large_imagenet1k",
        "gcvit_large_imagenet22k_384": "nvidia/tao/pretrained_gcvit_classification_imagenet:gcvit_large_imagenet22k_384",
        "fan_hybrid_base_in22k_1k_384": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_base_in22k_1k_384",
        "fan_hybrid_base_in22k_1k": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_base_in22k_1k",
        "fan_hybrid_base_in22k": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_base_in22k",
        "fan_hybrid_large_in22k_1k_384": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_large_in22k_1k_384",
        "fan_hybrid_large_in22k_1k": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_large_in22k_1k",
        "fan_hybrid_large_in22k_384": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_large_in22k_384",
        "fan_hybrid_large_in22k": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_large_in22k",
        "fan_hybrid_small": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_small",
        "fan_hybrid_tiny": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_tiny",
        "fan_hybrid_Xlarge_in22k": "nvidia/tao/pretrained_fan_classification_imagenet:fan_hybrid_Xlarge_in22k",
        "fan_base_hybrid_nvimagenet": "nvidia/tao/pretrained_fan_classification_nvimagenet:fan_base_hybrid_nvimagenet",
        "fan_small_hybrid_nvimagenet": "nvidia/tao/pretrained_fan_classification_nvimagenet:fan_small_hybrid_nvimagenet",
        "fan_large_hybrid_nvimagenet": "nvidia/tao/pretrained_fan_classification_nvimagenet:fan_large_hybrid_nvimagenet",
        "gcvit_xxtiny_nvimagenet": "nvidia/tao/pretrained_gcvit_classification_nvimagenet:gcvit_xxtiny_nvimagenet",
        "gcvit_xtiny_nvimagenet": "nvidia/tao/pretrained_gcvit_classification_nvimagenet:gcvit_xtiny_nvimagenet",
        "gcvit_tiny_nvimagenet": "nvidia/tao/pretrained_gcvit_classification_nvimagenet:gcvit_tiny_nvimagenet",
        "gcvit_small_nvimagenet": "nvidia/tao/pretrained_gcvit_classification_nvimagenet:gcvit_small_nvimagenet",
        "gcvit_base_nvimagenet": "nvidia/tao/pretrained_gcvit_classification_nvimagenet:gcvit_base_nvimagenet",
    },
    "classification_tf1": {
        "vgg19": "nvidia/tao/pretrained_classification:vgg19",
        "vgg16": "nvidia/tao/pretrained_classification:vgg16",
        "squeezenet": "nvidia/tao/pretrained_classification:squeezenet",
        "resnet50": "nvidia/tao/pretrained_classification:resnet50",
        "resnet34": "nvidia/tao/pretrained_classification:resnet34",
        "resnet18": "nvidia/tao/pretrained_classification:resnet18",
        "resnet101": "nvidia/tao/pretrained_classification:resnet101",
        "resnet10": "nvidia/tao/pretrained_classification:resnet10",
        "mobilenet_v2": "nvidia/tao/pretrained_classification:mobilenet_v2",
        "mobilenet_v1": "nvidia/tao/pretrained_classification:mobilenet_v1",
        "googlenet": "nvidia/tao/pretrained_classification:googlenet",
        "efficientnet_b1_swish": "nvidia/tao/pretrained_classification:efficientnet_b1_swish",
        "efficientnet_b1_relu": "nvidia/tao/pretrained_classification:efficientnet_b1_relu",
        "darknet53": "nvidia/tao/pretrained_classification:darknet53",
        "darknet19": "nvidia/tao/pretrained_classification:darknet19",
        "cspdarknet_tiny": "nvidia/tao/pretrained_classification:cspdarknet_tiny",
        "cspdarknet53": "nvidia/tao/pretrained_classification:cspdarknet53",
        "cspdarknet19": "nvidia/tao/pretrained_classification:cspdarknet19",
    },
    "classification_tf2": {
        "efficientdet-b4": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b4",
        "efficientdet-b5": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b5",
        "efficientdet-b3": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b3",
        "efficientdet-b2": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b2",
        "efficientdet-b1": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b1",
        "efficientdet-b0": "nvidia/tao/pretrained_efficientdet_tf2_nvimagenet:efficientnet-b0",
        "efficientnet_b0": "nvidia/tao/pretrained_classification_tf2:efficientnet_b0",
    },
}
