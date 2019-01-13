# d7_to_miraclp

## このスクリプトについて
WanhaoD7 Workshopで出力したCWSファイルをMIRACLPで出力可能な物に変換するスクリプトです。

##  WanhaoD7 WorkshopでのGCODE設定
以下のような感じで設定します。  

■header  
空にしておきます。  

■Start  
G21 ;Set units to be mm  
G92 X0 Y0 Z0  
G91 ;Relative Positioning  
M17 ;Enable motors  
G161 Z F100  
G92 Z0  
G1 Z5  
G161 Z F30  
G92 Z0  

■Layer  
;********** Pre-Slice Start ********  
;Set up any GCode here to be executed before a lift  
;********** Pre-Slice End **********  
M110 T0 S255  
;<Slice> [[LayerNumber]]  
;<Delay> [[exposureTime]]  
;<Slice> Blank  
M110 T0 S0  
;********** Lift Sequence ********  
G1 Z2.0 F100.0  
G1 Z-1.95 F200.0  
;<Delay> [[WaitAfterPrint]]  
;********** Lift Sequence **********  
  
■End  
;********** Footer Start ********  
;Here you can set any G or M-Code which should be executed after the last Layer is Printed  
M18 ;Disable Motors  
M110 T0 S0  
;<Completed>  
;********** Footer End ********  
  
■KillPrint  
空にしておきます。  
