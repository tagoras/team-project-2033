import UserPage from "./User";
function UserForm() {
  function addUserHandler(userData) {
    console.log(JSON.stringify(userData));
    fetch("/User", {
      method: "POST",
      body: JSON.stringify(userData),
    }).then(
      (value) => {
        console.log(value);
   ;
      }
    );
  }
  return (
    <section>
      <div className="login">
        <UserPage addUserForm={addUserHandler} />
      </div>
    </section>
  );
}
export default UserForm;
