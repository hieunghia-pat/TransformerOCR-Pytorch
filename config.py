## dataset configuartion
batch_size = 8
out_level = "character"
image_dir = "../UIT_HWDB_line_syn"
image_size = (1024, 64)

## training configuration
max_epoch = 500
learning_rate = 5e-4
checkpoint_path = "/content/gdrive/MyDrive/TransformerOCR/saved_models"
start_from = None
warmup = 2000

## model configuration
dropout = 0.5
num_layers = 4
d_model = 256
dff = 512
heads = 8
beam_size = 2

## objective function configuration
smoothing = 0.2

## configure for debug only
debug = True
save_per_iter = 100
tmp_checkpoint_path = "/content/gdrive/MyDrive/TransformerOCR/tmp_saved_models"