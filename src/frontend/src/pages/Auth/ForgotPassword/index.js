import { useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { useRouter } from 'next/router';
import { useAuth } from '../../../context/authContext';

const ForgotPassword = () => {
  const router = useRouter();
  const { forgotPassword } = useAuth();
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const formik = useFormik({
    initialValues: {
      email: '',
    },
    validationSchema: Yup.object({
      email: Yup.string().email('Invalid email address').required('Required'),
    }),
    onSubmit: async (values) => {
      try {
        await forgotPassword(values.email);
        setMessage('Password reset email sent successfully!');
        setError('');
      } catch (err) {
        setMessage('');
        setError(err.message);
      }
    },
  });

  return (
    <div>
      <h1>Forgot Password</h1>
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={formik.handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.email}
        />
        {formik.touched.email && formik.errors.email ? (
          <p style={{ color: 'red' }}>{formik.errors.email}</p>
        ) : null}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ForgotPassword;

