# Probabilistic Safety Verification: A Situation Coverage Grid Approach

## Description

This project presents a method for the **probabilistic safety verification of autonomous vehicles** through systematic situation extraction, probabilistic modeling, and formal verification. The approach is centered on the concept of a **Situation Coverage Grid (SCG)** — a structured representation that exhaustively enumerates relevant environmental configurations affecting the vehicle’s behavior.

We extend this grid with **quantitative probabilistic data** collected from simulations or real-world operation. From this enriched model, a **probabilistic transition system** is automatically generated and verified against safety properties derived from a formal **hazard analysis**, specified using **temporal logic** (e.g., PCTL).

This enables:

* **Quantitative safety guarantees**
* **Early detection of critical scenarios**
* **Support for compliance** with industry safety standards (e.g., ISO 21448, UL 4600)

<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/ecaef262-7e3f-42eb-bf0b-212a8b67e3cd" />
</p>

---

## Case Study: Autonomous Ground Vehicle (AGV) in a Warehouse

We illustrate the feasibility of our approach using a case study where an **Autonomous Ground Vehicle (AGV)** operates within a warehouse environment, patrolling a set of designated locations. The safety of this AGV is verified based on the exhaustive analysis of potential warehouse situations.

### Repository Structure

All components of the methodology are organized in the following directories:

* [`./example-AGV/odm/`](./example-AGV/odm/)
  **Operational Design Domain (ODD)** description, including environment and object decompositions.

* [`./example-AGV/ascg/`](./example-AGV/ascg/)
  The **Augmented Situation Coverage Grid (ASCG)**, including the SCG, situation enumeration and additional collected **probabilistic data** (e.g., transition frequencies, observation logs) used to annotate the SCG.
  
* [`src/run_dtmc.py`](./src/run_dtmc.py/)
  Script for generating the **probabilistic model**, DTMC (Discrete Time Markov Chain), from the ASCG.
  
* [`./example-AGV/gen-model/`](./example-AGV/gen-model/)
  **Probabilistic model** generated in the PRISM language.
  
* [`./example-AGV/properties/`](./example-AGV/properties/)
  Formal **safety properties** expressed in temporal logic, derived from a hazard analysis of the AGV operation.
  
* [`./example-AGV/prism-results/`](./example-AGV/prism-results/)
   **Verification results**, summary of verification outcomes and visual analytics. Script for the automated generation of such report available at [`./src/prism-results/get_results.py`](./src/prism-results/get_results.py). Results file prism_results.txt is obtained through the verification of the DTMC model under probabilistic safety properties defined in [`./example-AGV/properties/`](./example-AGV/properties/), each representing a situation as an initial state.
   
   Verification is performed using the **PRISM probabilistic model checker**, enabling automated quantitative safety analysis of the ASCG.

---

## How to Run

To create the probabilistic model, provide the link to the ASCG provided as a CSV file (see )
   ```
   python run_dtmc.py <path_to_augmented_grid_csv_file>
   ```

---

## Dependencies

* Python 3.8+
* PRISM Model Checker ([https://www.prismmodelchecker.org/](https://www.prismmodelchecker.org/))
* Pandas



