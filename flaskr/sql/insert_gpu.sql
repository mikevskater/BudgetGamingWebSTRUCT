INSERT INTO gpu 
        (
         gpu_vramType, 
         gpu_vramSize,
         gpu_slotWidth,
         gpu_interface,
         gpu_6pin,
         gpu_8pin,
         gpu_clockSpeed,
         gpu_memClockSpeed,
         gpu_busBandwidth,
         gpu_crossfire,
         gpu_sli,
         gpu_pcPart_id,
         gpu_pcBuild_id
         ) 
        VALUES (
                ?, 
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
                )