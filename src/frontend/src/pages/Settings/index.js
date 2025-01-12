import { useSession } from '@auth0/nextjs-auth0';

export default function Settings() {
  const { getSession } = useSession();

  return (
    <div>
      <h1>Settings</h1>
      <p>This is the settings page.</p>
    </div>
  );
}

