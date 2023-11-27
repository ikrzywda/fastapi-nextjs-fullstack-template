import { IconButton, Stack, Typography } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

interface TodoListsHeaderProps {
  onAddClick: () => void;
}

const TodoListsHeader = ({ onAddClick }: TodoListsHeaderProps) => {
  return (
    <Stack justifyContent="space-between" direction="row" width="100%">
      <Typography variant="h4">Todo Lists</Typography>
      <IconButton onClick={onAddClick}>
        <AddIcon />
      </IconButton>
    </Stack>
  );
};

export default TodoListsHeader;
