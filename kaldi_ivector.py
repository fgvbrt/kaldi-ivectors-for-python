import os
import numpy as np
dir_name = os.path.dirname(os.path.realpath(__file__))


def train(feat_file, model_dir, M, ivector_dim=300, num_gselect=None):
    """
    This function will call the Bash script to train an i-vector extractor (and its corresponding UBM)
    Inputs:
        feat_file: Path to the Kaldi script (.spc) file with the features to use for i-vector training
        model_dir: Path where the model will be stored. It will create a sub-folder according to the number of Gaussians.
        M: Number of Gaussians in the UBM
        ivector_dim: dimension of the i-vectors
        num_gselect: Number of gaussians for the gaussian selection process

    Returns:
        num_gselect: Number of gaussians for the gaussian selection process so it can be used during the i-vectors extraction
    """
    if num_gselect is None or ivector_dim is None:
        k = int(np.log2(M))
    if num_gselect is None:
        num_gselect = k + 1
    os.system(os.path.join(dir_name, "train_ivector_models.sh") + " " + str(M) + " " + str(ivector_dim) + " " + str(
        num_gselect) + " " + feat_file + " " + model_dir)
    return num_gselect


def extract(src_dir, feat_file, ivectors_dir, num_gselect):
    """
    The Bash script checks if the i-vectors have been extracted already.
    Inputs:
        src_dir: Model with the i-vector extractor (generated with train_ivector_models)
        feat_file: Path to the Kaldi script (.spc) file with the features to use for i-vector training
        ivectors_dir: Path where the i-vectors will be stored
        num_gselect: Number of gaussians for the gaussian selection process. Should be the same as in train
    Returns:
        str - scp filename with ivectors
    """
    os.system(os.path.join(dir_name, "extract_ivectors.sh") + " --num-gselect " + str(
        num_gselect) + " " + src_dir + " " + feat_file + " " + ivectors_dir)
    return os.path.join(ivectors_dir, 'ivector.scp')

