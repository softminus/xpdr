#include "Vtop.h"
#include "verilated.h"
#include "verilated_vcd_c.h"


int main(int argc, char **argv, char **env) {
  int i;
  int clk;
  Verilated::commandArgs(argc, argv);
  // init top verilog instance
  Vtop* top = new Vtop;
  // init trace dump
  Verilated::traceEverOn(true);
  VerilatedVcdC* tfp = new VerilatedVcdC;
  top->trace (tfp, 99);
  tfp->open ("top.vcd");
  // initialize simulation inputs
  top->crystal = 1;
  // run simulation for 1000 crystal periods
  for (i=0; i<1000; i++) {
    // dump variables into VCD file and toggle crystal
    for (clk=0; clk<2; clk++) {
      tfp->dump (2*i+clk);
      top->crystal = !top->crystal;
      top->eval ();
    }
    if (Verilated::gotFinish())  exit(0);
  }
  tfp->close();
  exit(0);
}
