from roboflow import Roboflow


def load_traffic_dataset(api_key):
    """
    Loads the UA-DETRAC traffic dataset from Roboflow
    """

    rf = Roboflow(api_key=api_key)

    project = rf.workspace("rjacaac1").project("ua-detrac-dataset-10k")

    dataset = project.version(1).download("yolov8")

    return dataset


def load_emergency_dataset(api_key):
    """
    Loads the emergency vehicle dataset from Roboflow
    """

    rf = Roboflow(api_key=api_key)

    project = rf.workspace("jam-hyzhb").project("object-detection-xdvt2")

    dataset = project.version(1).download("yolov8")

    return dataset
