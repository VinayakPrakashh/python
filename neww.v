`timescale 1ns / 1ps
module textbench;
reg a,b,c,d; 
wire e,f,g,h,i;
binary_to_bcd dut(a,b,c,d,e,f,g,h,i);
initial
begin
$monitor($time,"a=%b,b=%b,c=%b,d=%b,e=%b,f=%b,g=%b,h=%b,i=%b",a,b,c,d,e,f,g,h,i);
#100 a=0;b=1;c=0;d=1;
#100 c=1;
#100 a=1;b=0;c=0;
#100 c=1;d=0;
#100 b=1;c=0;d=0;
#100 $finish;
end
endmodule





