import Header from './Header';
import StudentProfileCard from './StudentProfileCard';
import Footer from './Footer';

function App() {
  return (
    <div>
      <Header />
      <StudentProfileCard
        name="Salman"
        department="Computer Science Engineering (AI & DS)"
        college="B.S. Abdur Rahman Crescent Institute"
        email="240171601053@crescent.education"
      />
      <StudentProfileCard
        name="Abdullah"
        department="Computer Science Engineering"
        college="B.S. Abdur Rahman Crescent Institute"
        email="abdullah@example.com"
      />
      <StudentProfileCard
        name="Vijay"
        department="Computer Science Engineering"
        college="B.S. Abdur Rahman Crescent Institute"
        email="vijay@example.com"
      />
      <Footer />
    </div>
  );
}
export default App;