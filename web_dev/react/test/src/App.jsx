import {useState} from "react";

function App() {
  const [todos,setToDos]=useState([{
    title: "Study DSA",
    descrip: "from 5 to 7 pm"
  },{
    title: "Go for a walk",
    descrip: "from 7 to 8 pm"
  }]);
  return (
    <div>
      <button onClick={()=>{
        setToDos([...todos,{
          title: "New Todo",
          descrip: "descrip of new todo"
        }])
      }}>Click to add new todo</button>
      {todos.map((todo)=>{
        return <TodoComp title={todo.title} descrip={todo.descrip} />
      })}
    </div>
  )
}
function TodoComp(props){
  return (
    <div>
      <h1>{props.title}</h1>
      <h2>{props.descrip}</h2>
    </div>
  )
}

export default App
