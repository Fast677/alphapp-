import { useSession } from '@auth0/nextjs-auth0';

export default function CreateProject() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Create Project</h1>
      <p>This is the create project page.</p>
    </div>
  );
}

