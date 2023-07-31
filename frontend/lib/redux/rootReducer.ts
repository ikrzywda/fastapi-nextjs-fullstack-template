/* Instruments */
import { emptySlitApi } from "./api/emptyApi";
import { counterSlice } from "./slices";

export const reducer = {
  counter: counterSlice.reducer,
  api: emptySlitApi.reducer,
};
