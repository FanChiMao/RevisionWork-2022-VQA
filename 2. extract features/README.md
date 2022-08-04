# Extract features  

## Extract features  
Run the code [extract.py](./extract.py) to generate extracted features (the other codes are my senior's codes)  
> Notice  
> - Confirm the path including the data generated from previous process
> - Confirm the video resolution in line 43 and video number in L44, L47.  

The keypoint in this process is, you have to change the annotation in `extract.py` to generate corresponding features.  
That is, the col, row, and frames and the differnt layers of extrating model.  

***
Finally, you have to generate 18 feature files (3 * 6):  
- extracted_features_previous_pool_layer_DATASET.mat
- extracted_features_previous1_pool_layer_DATASET.mat
- extracted_features_previous2_pool_layer_DATASET.mat
- extracted_features_previous3_pool_layer_DATASET.mat
- extracted_features_previous4_pool_layer_DATASET.mat
- extracted_features_previous5_pool_layer_DATASET.mat
- extracted_features_row_t_previous_pool_layer_DATASET.mat
- extracted_features_row_t_previous1_pool_layer_DATASET.mat
- extracted_features_row_t_previous2_pool_layer_DATASET.mat
- extracted_features_row_t_previous3_pool_layer_DATASET.mat
- extracted_features_row_t_previous4_pool_layer_DATASET.mat
- extracted_features_col_t_previous5_pool_layer_DATASET.mat
- extracted_features_col_t_previous1_pool_layer_DATASET.mat
- extracted_features_col_t_previous2_pool_layer_DATASET.mat
- extracted_features_col_t_previous3_pool_layer_DATASET.mat
- extracted_features_col_t_previous4_pool_layer_DATASET.mat
- extracted_features_col_t_previous5_pool_layer_DATASET.mat

> Notice  
> previous  => `mixed9` in line 36  
> previous1 => `mixed8` in line 36  
> previous2 => `mixed7` in line 36  
> previous3 => `mixed6` in line 36  
> previous4 => `mixed5` in line 36  
> previous5 => `mixed4` in line 36  
