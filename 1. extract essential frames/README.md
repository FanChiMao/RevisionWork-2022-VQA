# Extract essential frames  

## Extract frame  
Run the code [extract_frame.m](./1.%20extract%20essential%20frames/extract_frame.m) to generate the essential frame of each video (xlsx).  
Then run the [save_detail.m](./1.%20extract%20essential%20frames/save_detail.m) to get the relationship bwtween frame type and video (xlsx).  
> Notice
> - Confirm the correct video (yuv or mp4 file) path and run.  
> - The video size (resolution) should be the same size.  

## Extract STS  
Run the code [extract_frame_STS.m](./1.%20extract%20essential%20frames/extract_frame_STS.m) to get the STS frame of each video (xlsx).  

## Generate the ground-truth (DMOS) file  
Run the code [sorted_DMOS.m](./1.%20extract%20essential%20frames/sorted_DMOS.m) to generate the GT DMOS file (xlsx).  
> Notice
> - Confirm the correct video (yuv or mp4 file) path and run.  
> - The video size (resolution) should be the same size.  

In the end of this process you will generate 5 data:  
- extract_frame_num4_without_low_value_60_DATASET.xlsx  
- extract_frame_num_col_t_ave_60_DATASET.xlsx  
- extract_frame_num_row_t_ave_60_DATASET.xlsx  
- frames_details_DATASET.xlsx  
- sorted_DMOS_DATASET.xlsx  
