import axios from "axios";
import React, { useState } from "react";
const END_POINT = "https://enigmatic-cove-02207.herokuapp.com/getGraph";

export default function App() {
  const defaultState = {
    currentlySelected: "cube",
    start: "0",
    end: "10",
    increment: "1",
    imageData: "",
  };
  const [state, setState] = useState(defaultState);
  return (
    <div className="App">
      <select
        value={state.currentlySelected}
        onChange={(e) => {
          setState({
            ...state,
            currentlySelected: e.target.value,
          });
        }}
      >
        <option value="linear">y = x</option>
        <option value="square">y = x2</option>
        <option value="cube">y = x3</option>
      </select>
      <br />
      {["start", "end", "increment"].map((currentElement) => {
        return (
          <div key={currentElement.toString()}>
            <label>{currentElement}ing from: </label>
            <input
              type="number"
              value={state[currentElement].toString()}
              onChange={(e) => {
                setState({
                  ...state,
                  [currentElement]: e.target.value,
                });
              }}
            />
          </div>
        );
      })}
      <br />
      <button
        onClick={async () => {
          if (
            !state.currentlySelected ||
            !state.increment ||
            !state.start ||
            !state.end
          ) {
            console.error("No value cannot be falsy");
            return;
          }
          // real code is here
          try {
            const config = {
              headers: {
                "Content-Type": "application/json",
              },
            };
            const { start, end, increment, currentlySelected } = state;
            const body = {
              start,
              end,
              increment,
              inputFunction: currentlySelected,
            };
            console.log("body is", body);
            const imageData = (
              await axios.post("/api/mat", JSON.stringify(body), config)
            ).data;
            console.log("imageData is", imageData["finalData"]);
            const finalImageData = imageData?.["finalData"] ?? "";
            setState({
              ...state,
              imageData: finalImageData,
            });
          } catch (err) {
            console.error(err);
            console.error(err.message);
          }
        }}
      >
        Send Data
      </button>
      <button onClick={() => console.log("state is", state)}>
        Click to state
      </button>
      {state.imageData.length !== 0 && (
        <img src={`data:image/png;base64,${state.imageData}`} alt="something" />
      )}
    </div>
  );
}
