/* Instruments */
import { emptySplitApi } from "./api/emptyApi";
import { counterSlice } from "./slices";

export const reducer = {
  counter: counterSlice.reducer,
  api: emptySplitApi.reducer,
};
