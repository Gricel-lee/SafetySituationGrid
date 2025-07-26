import pandas as pd
import os


import pandas as pd
import os

def create_folder(fpath, name):
    # Get the directory from the file path
    dir_path = os.path.join(os.path.dirname(fpath), name)

    # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)  # `exist_ok=True` avoids errors if the directory already exists
    
    return dir_path

def generate_prism_file(fpath, init_state=1):
    df = pd.read_csv(fpath, index_col=False)
    
    # get file name
    fname = os.path.basename(fpath)
    
    # create "output" folder
    output_folder = create_folder(fpath, "gen-output")

    prism_file = os.path.join(output_folder, f"{fname.split('.')[0]}.prism")

    # Change Situation column name, remove 's' leaving only the number
    df["Situation"] = df["Situation"].str.replace("s", "", regex=False).astype(int)
    
    # Group transitions by State ID and Action
    transitions = {}
    for _, row in df.iterrows():
        state = row['Situation']
        action = row['Action']
        next_state = row['Next Situation']
        prob = row['Probability']

        if (state, action) not in transitions:
            transitions[(state, action)] = []
        transitions[(state, action)].append((next_state, prob))
        
    # Write PRISM model
    with open(prism_file, 'w') as f:
        f.write('dtmc\n\n')
        f.write('module Robot\n')
        f.write(f'  s : [0..{df["Situation"].max()}] init {init_state};\n\n')

        # Add transitions
        for (state, action), outcomes in transitions.items():
            f.write(f'  // State {state}, Action: {action}\n')
            f.write(f'  [{action.replace(" ","")}] s={state} -> ')
            probs = []
            for next_state, prob in outcomes:
                probs.append(f'{prob}:(s\'={next_state})')
            f.write(' + '.join(probs))
            f.write(';\n\n')

        f.write('endmodule\n')
    return prism_file


import pandas as pd
import os

def convert_xlsx_to_csv(xlsx_file):
    try:
        # Extract the directory and file name (without extension)
        directory, filename = os.path.split(xlsx_file)
        basename, _ = os.path.splitext(filename)
        
        # Construct the output file path with the same name but .csv extension
        csv_file = os.path.join(directory, f"{basename}.csv")
        
        # Read/write file
        df = pd.read_excel(xlsx_file)
        df.to_csv(csv_file, index=False)
        
        print(f"Successfully converted {xlsx_file} to {csv_file}")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    
    return csv_file


# Run file from command line
if __name__ == "__main__":
    import sys
    # Read augmented situation coverage grid file path
    if len(sys.argv) > 1:
        fpath = sys.argv[1]
    else:
        print("Usage: python run_dtmc.py <path_to_augmented_grid_csv_file>")
        sys.exit(1)

    # Generate PRISM file
    prism_file = generate_prism_file(fpath, init_state=1)
    
    print("\nPRISM model saved in: "+prism_file)

# >> Example usage: <<
# python3 ./WildRob/run_dtmc.py "/home/gnvf500/Gricel-Documents/GithubGris/SafetySituationGrid/example-AGV/coverageGrid.csv"