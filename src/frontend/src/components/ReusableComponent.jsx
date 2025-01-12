import React from 'react';

const ReusableComponent = ({ children, className }) => {
  return (
    <div className={className}>
      {children}
    </div>
  );
};

export default ReusableComponent;

