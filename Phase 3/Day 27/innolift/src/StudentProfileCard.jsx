function StudentProfileCard(props) {
  return (
    <div className="profile-card">
      <p><strong>Name:</strong> {props.name}</p>
      <p><strong>Department:</strong> {props.department}</p>
      <p><strong>College:</strong> {props.college}</p>
      <p><strong>Email:</strong> {props.email}</p>
    </div>
  );
}
export default StudentProfileCard;