import { useRouter } from 'next/router';

export default function ViewProject() {
  const router = useRouter();
  const { projectId } = router.query;

  return (
    <div>
      <h1>View Project: {projectId}</h1>
      <p>This is the view project page for project ID: {projectId}</p>
    </div>
  );
}

